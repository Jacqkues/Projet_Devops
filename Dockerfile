FROM nginx:latest
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY ./static /usr/share/nginx/html/
COPY ./static /etc/nginx/html;