These are the files used to run a discord bot for swmud.org that checks and returns remaining mud boot time.

fetchmud.sh runs at a regular interval, connects to swmud, and writes uptime (in seconds) to a file

discobot.py is the bot itself and listens for /uptime, /helpme, or /reboot on the swmud discord server

/uptime runs mudup.sh and up2disco.py

/reboot runs mudbc.sh and boot2disco.py


discobot_keepalive.sh runs every 10 mins, checks to see if discobot.py is running. if not, discobot.py is called.

Example Usage:
mudup/mudbc.sh checks the uptime in seconds, calculates how much time has elapsed since uptime was written,
up2disco/boot2disco returns the value to discord via a webhook
