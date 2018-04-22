FROM python:3.6.3
LABEL maintainer "ricardobchaves6@gmail.com"

RUN mkdir /cron 
RUN mkdir /watch

ADD . /cron

WORKDIR /cron

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
