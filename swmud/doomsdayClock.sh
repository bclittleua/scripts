#!/bin/bash
#check reboot.csv, append time elapsed AND
#IF timeRem =< 600 THEN
##shout a warning to discord via webhook

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
echo $totalRem > /home/pi/bin/mud/sw-rb.log

#determine whether or not to send a warning to discord
if [ "$secsUp" -ge "628200" ]; then
	#call the DoomSayer to return calculated uptime to discord via webhook
	sleep 2 | sudo python3.6 /home/pi/bin/mud/doomsayer.py $totalRem
fi

