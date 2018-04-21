# Remove Old Dirs

[![Build Status](https://travis-ci.org/ricardochaves/docker_cron_remove_old_dirs.svg?branch=master)](https://travis-ci.org/ricardochaves/docker_cron_remove_old_dirs)

[![Coverage Status](https://coveralls.io/repos/github/ricardochaves/docker_cron_remove_old_dirs/badge.svg?branch=master)](https://coveralls.io/github/ricardochaves/docker_cron_remove_old_dirs?branch=master)

Monitor multiple directories and remove all directories older than X times.

## How to use

You just need to create a ```docker-compose.yml``` with the following configuration.


```
version: "3.5"
services:
  web:
    image: ricardobchaves6/docker-cron-remove-dirs
    environment:
      - SLEEP_TIME_SECONDS=2
      - TIME_TO_REMOVE_SECONDS=2
    volumes:
      - ./to_watch_1:/watch
      - ./to_watch_2:/watch
    command: ["/cron/script.sh"]
```