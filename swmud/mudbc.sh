#!/bin/bash
#this script runs when discobot.py is asked for /uptime

#calculates time elapsed since reboot.csv was written
uptime=$(cat /home/pi/bin/mud/reboot.csv)
elapsed=$(echo  $(( $(date +%s) - $(date --reference /home/pi/bin/mud/reboot.csv +%s) )) )

#adds time elapsed to uptime (seconds)
secsUp=$(($uptime + $elapsed))
#begin calculation of time remaining
secsRem=$((630000 - $secsUp))
daysRem=$(($secsRem / 86400))
hoursRem=$(( $(($secsRem / 3600)) - $(($daysRem * 24)) ))
minsRem=$(( $(($secsRem / 60)) - $(($hoursRem * 60)) - $(($daysRem *1440)) ))
#result
totalRem=$(echo $daysRem"D"$hoursRem"H"$minsRem"M")

#call the boot2disco.py to return calculated uptime to user
sleep 2 | sudo python3.6 /home/pi/bin/mud/boot2disco.py $totalRem
