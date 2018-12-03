#!/bin/bash
#this script runs when discobot.py is asked for /uptime

#calculates time elapsed since reboot.csv was written
uptime=$(cat /home/pi/bin/mud/reboot.csv)
elapsed=$(echo  $(( $(date +%s) - $(date --reference /home/pi/bin/mud/reboot.csv +%s) )) )

#adds time elapsed to uptime (seconds)
secsUp=$(($uptime + $elapsed))
#begin calculation of time remaining
secsRem=$((630000 - $secsUp))
daysUp=$(($secsUp / 86400))
hoursUp=$(( $(($secsUp / 3600)) - $(($daysUp * 24)) ))
minsUp=$(( $(($secsUp / 60)) - $(($hoursUp * 60)) - $(($daysUp *1440)) ))
#result
totalUp=$(echo $daysUp"D"$hoursUp"H"$minsUp"M")

#call the boot2disco.py to return calculated uptime to user
sleep 2 | sudo python3.6 /home/pi/bin/mud/up2disco.py $totalUp
