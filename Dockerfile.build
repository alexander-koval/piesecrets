FROM python:3
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system --deploy --dev --ignore-pipfile

COPY . /code/