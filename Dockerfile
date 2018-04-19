FROM python:3.6.3
LABEL maintainer "ricardobchaves6@gmail.com"

RUN pip install arrow

RUN mkdir /cron 
