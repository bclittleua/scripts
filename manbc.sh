#!/bin/bash
#SHELL=/bin/bash
#PATH=/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin
#
sleep 3 | telnet swmud.org 6666 > /home/pi/bin/man/manprompt-output.log
#
grep "SWmud has been up for" /home/pi/bin/man/manprompt-output.log > /home/pi/bin/man/prompt
tr -d '[:space:]' </home/pi/bin/man/prompt > /home/pi/bin/man/uptime
sed -e "s/SWmudhasbeenupfor/ /g" -i /home/pi/bin/man/uptime
uptimeRaw=$(cat /home/pi/bin/man/uptime)
uptimeCSV=$(echo "$uptimeRaw" | sed 's/[[:alpha:]]/,/g'|sed 's/.$//')
IFS="," read -a arr <<< "$uptimeCSV"
#NOTE: arr[0]=days arr[1]=hours arr[2]=minutes
#NOTE: 7d=604800s, 7h=25200s, 1boot=630000s
#MATH BELOW!
secsUp=$(($((${arr[0]} * 86400)) + $((${arr[1]} * 3600)) + $((${arr[2]} * 60))))
secsRem=$((630000 - $secsUp))
daysRem=$(($secsRem / 86400))
hoursRem=$(($(($secsRem / 3600)) - $(($daysRem * 24))))
minsRem=$(($(($secsRem /60)) - $(($hoursRem * 60)) - $(($daysRem * 1440))))
outmsg=$(echo $daysRem"D"$hoursRem"H"$minsRem"M")
#
sleep 2 | sudo python3 /home/pi/bin/man/boot2disco.py $outmsg
#
echo "SWmud has been up for" $uptimeRaw
echo $outmsg
