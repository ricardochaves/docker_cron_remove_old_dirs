#!/bin/bash
echo "******************************************************"
echo "Application started with configuration:"
echo "SLEEP_TIME_SECONDS=$SLEEP_TIME_SECONDS"
echo "TIME_TO_REMOVE_SECONDS=${TIME_TO_REMOVE_SECONDS}"
echo "******************************************************"

while sleep $SLEEP_TIME_SECONDS; do (./cron/ep.sh &) ; done