openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout nginx-selfsigned.key -out nginx-selfsigned.crt
openssl dhparam -out dhparam.pem 4096
ufw enable 443/tcp
ufw enable 443/udp
