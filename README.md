# Remove Old Dirs

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