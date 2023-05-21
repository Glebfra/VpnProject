FROM python:3.10.6-alpine

COPY . /app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk --update add \
        bash \
        gcc \
        zlib-dev \
        git \
        linux-headers \
        build-base \
        musl \
        musl-dev \
        memcached \
        libmemcached-dev

RUN pip install -r requirements.txt

CMD uwsgi --http :8000 --wsgi-file ./app/wsgi.py --enable-threads
