#!/bin/bash
#this script runs once every 2 hours to fetch uptime from swmud.org:6666

#Connect to mud and copy the prompt to a log file
sleep 3 | telnet swmud.org 6666 > /home/pi/bin/mud/capture.log

#parse out the uptime from the prompt.log, remove spaces and alphas, convert DayHourMin to CSV
grep "SWmud has been up for" /home/pi/bin/mud/capture.log > /home/pi/bin/mud/prompt
tr -d '[:space:]' </home/pi/bin/mud/prompt > /home/pi/bin/mud/uptime
sed -e "s/SWmudhasbeenupfor/ /g" -i /home/pi/bin/mud/uptime
uptimeRaw=$(cat /home/pi/bin/mud/uptime)
uptimeCSV=$(echo "$uptimeRaw" | sed 's/[[:alpha:]]/,/g'|sed 's/.$//')
IFS="," read -a arr <<< "$uptimeCSV"

#converts uptime to seconds and writes to a file for discobot.py to reference
secsUp=$(($((${arr[0]} * 86400)) + $((${arr[1]} * 3600)) + $((${arr[2]} * 60))))
echo $secsUp > /home/pi/bin/mud/reboot.csv
