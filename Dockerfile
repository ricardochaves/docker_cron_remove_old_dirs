FROM python:3.6.3
LABEL maintainer "ricardobchaves6@gmail.com"

RUN pip install -r requirements.txt

RUN mkdir /cron 
RUN mkdir /watch

ADD . /cron