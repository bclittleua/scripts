#!/bin/bash
#SHELL=/bin/bash
#PATH=/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin

sleep 3 | telnet swmud.org 6666 > /home/pi/bin/manprompt-output.log
#grep "SWmud has been up for" /home/pi/bin/prompt-output.log > /var/www/html/index.html
grep "SWmud has been up for" /home/pi/bin/manprompt-output.log > /home/pi/bin/preMan

tr -d '[:space:]' </home/pi/bin/preMan >/home/pi/bin/uptimeMan
sed -e "s/SWmudhasbeenupfor/ /g" -i /home/pi/bin/uptimeMan
sed  's/[A-Za-z]*/ /g' -i /home/pi/bin/uptimeMan | IFS=' ' read -r -a array <<< "$string"



uptimeRaw=$(cat /home/pi/bin/uptimeMan)

echo $uptimeRaw
