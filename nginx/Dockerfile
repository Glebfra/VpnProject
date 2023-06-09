FROM nginx

ADD ./nginx.conf /etc/nginx/nginx.conf
ADD ./uwsgi_params /etc/nginx/uwsgi_params
ADD ./django_nginx.conf /etc/nginx/sites-available/django_nginx.conf
ADD ./front_nginx.conf /etc/nginx/sites-available/front_nginx.conf

RUN rm /etc/nginx/conf.d/default.conf

RUN mkdir /etc/nginx/sites-enabled
RUN ln -s /etc/nginx/sites-available/django_nginx.conf /etc/nginx/sites-enabled/
RUN ln -s /etc/nginx/sites-available/front_nginx.conf /etc/nginx/sites-enabled

EXPOSE 80
EXPOSE 443
CMD ["nginx"]
