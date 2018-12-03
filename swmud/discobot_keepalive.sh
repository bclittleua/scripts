#!/bin/bash
for pid in $(pidof -x discobot.py); do
    if [ $pid != $$ ]; then
        exit 1
    fi
done
sudo python3.6 /home/pi/bin/discords/discobot.py &
