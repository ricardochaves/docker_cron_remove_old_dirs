# Remove Old Dirs

[![Build Status](https://travis-ci.org/ricardochaves/docker_cron_remove_old_dirs.svg?branch=master)](https://travis-ci.org/ricardochaves/docker_cron_remove_old_dirs) [![Coverage Status](https://coveralls.io/repos/github/ricardochaves/docker_cron_remove_old_dirs/badge.svg)](https://coveralls.io/github/ricardochaves/docker_cron_remove_old_dirs) [![](https://images.microbadger.com/badges/version/ricardobchaves6/docker-cron-remove-dirs.svg)](https://microbadger.com/images/ricardobchaves6/docker-cron-remove-dirs "Get your own version badge on microbadger.com") [![](https://images.microbadger.com/badges/image/ricardobchaves6/docker-cron-remove-dirs.svg)](https://microbadger.com/images/ricardobchaves6/docker-cron-remove-dirs "Get your own image badge on microbadger.com")

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
      - /mydir/cron1:/cron/watch/cron_1
      - /mydir/cron2:/cron/watch/cron_2
```

With the above configuration it will keep looking at everything you have inside ```cron1``` and ```cron2```. Any directory within these two that is older than the configured time will be deleted.
