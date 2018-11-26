These are the files used to run a discord bot for swmud.org that checks and returns remaining mud boot time.


discobot.py is the bot itself and listens for /uptime on the swmud discord server to run manbc.sh

manbc.sh briefly connects to mud and grabs uptime from login prompt

uptime is subtracted from 7d7h for time remaining until reboot

manbc.sh then calls boot2disco.py which sends the remaining time to discord via webhook


bootcheck.sh is setup to return only the uptime vs time remaining
