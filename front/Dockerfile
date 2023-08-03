FROM node:18-alpine

RUN mkdir /etc/front
WORKDIR /etc/front

COPY . /etc/front

RUN npm i
RUN npm run build
