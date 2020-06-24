FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

# RUN rm /etc/ssl/piesecrets.crt
COPY piesecrets.crt /etc/ssl/

# RUN rm /etc/ssl/piesecrets.key
COPY piesecrets.key /etc/ssl/