#!/bin/bash
#SHELL=/bin/bash
#PATH=/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin

sleep 3 | telnet swmud.org 6666 > /home/pi/bin/prompt-output.log
grep "SWmud has been up for" /home/pi/bin/prompt-output.log > /var/www/html/index.html
grep "SWmud has been up for" /home/pi/bin/prompt-output.log > /home/pi/bin/preUp
tr -d '[:space:]' </home/pi/bin/preUp >/home/pi/bin/uptime
sed -e "s/SWmudhasbeenupfor//g" -i /home/pi/bin/uptime
uptimeRaw=$(cat /home/pi/bin/uptime)
sleep 2 | sudo python3 /home/pi/bin/boot2disco.py $uptimeRaw
echo $uptimeRaw
