FROM python:3.8-slim as base
ENV PYROOT /pyroot
ENV PYTHONUSERBASE $PYROOT

FROM base as builder
RUN pip install pipenv==2018.10.13

RUN mkdir /code
WORKDIR /code
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv==2018.10.13 && \
  apt update && \
  apt install -y --no-install-recommends gcc python3-dev libssl-dev && \
  PIP_USER=1 PIP_IGNORE_INSTALLED=1 \
  pipenv install --deploy --system --ignore-pipfile && \
  apt remove -y gcc python3-dev libssl-dev && \
  apt autoremove -y && \
  pip uninstall pipenv -y

FROM base
COPY --from=builder $PYROOT/lib $PYROOT/lib
COPY --from=builder $PYROOT/bin $PYROOT/bin
ENV PATH $PATH:$PYROOT/bin/
ENV PIPENV_ROOT $PYROOT/lib/python3.8/site-packages
#ENV PYTHONWRITEBYTECODE 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /var/log/piesecrets
WORKDIR /code
COPY Pipfile Pipfile.lock /code/
COPY . /code/
# ADD ./media /code/media/



# FROM python:3-slim

# # ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# RUN mkdir /code
# WORKDIR /code

# # both files are explicitly required!
# COPY Pipfile Pipfile.lock /code/

# RUN pip install pipenv==2018.10.13 && \
#   apt update && \
#   apt install -y --no-install-recommends gcc python3-dev libssl-dev && \
#   pipenv install --deploy --system --ignore-pipfile && \
#   apt remove -y gcc python3-dev libssl-dev && \
#   apt autoremove -y && \
#   pip uninstall pipenv -y

# COPY . /code/

# # CMD ["python", "app.py"]