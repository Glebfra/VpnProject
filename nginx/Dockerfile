FROM nginx

ADD ./nginx.conf /etc/nginx/nginx.conf
ADD ./uwsgi_params /etc/nginx/uwsgi_params
ADD ./django_nginx.conf /etc/nginx/sites-available/django_nginx.conf
ADD ./front_nginx.conf /etc/nginx/sites-available/front_nginx.conf
ADD ./nginx-selfsigned.key /etc/nginx/nginx-selfsigned.key
ADD ./nginx-selfsigned.crt /etc/nginx/nginx-selfsigned.crt
ADD ./self-signed.conf /etc/nginx/snippets/self-signed.conf
ADD ./ssl-params.conf /etc/nginx/snippets/ssl-params.conf
ADD ./dhparam.pem /etc/nginx/dhparam.pem

RUN rm /etc/nginx/conf.d/default.conf

RUN mkdir /etc/nginx/sites-enabled
RUN ln -s /etc/nginx/sites-available/django_nginx.conf /etc/nginx/sites-enabled/
RUN ln -s /etc/nginx/sites-available/front_nginx.conf /etc/nginx/sites-enabled

RUN cd /etc/nginx

EXPOSE 80
EXPOSE 443
CMD ["nginx"]
