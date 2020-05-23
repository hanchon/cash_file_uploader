#!/usr/bin/env sh
while true; do
  tail -f /dev/null & wait ${!}
done