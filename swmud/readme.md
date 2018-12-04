These are the files used to run a discord bot for swmud.org that checks and returns current/remaining mud boot time.
  * fetchmud.sh runs at a regular interval, connects to swmud, and captures uptime (in seconds) to a file
  * discobot.py is the bot itself and listens for /uptime, /helpme, or /reboot on the swmud discord server
      * /uptime runs mudup.sh, which writes to sw-up.log, then returns the sw-up.log value
      * /reboot runs mudbc.sh, which writes to sw-rb.log, then returns the sw-rb.log value
  * discobot_keepalive.sh runs every 10 mins, checks to see if discobot.py is running. if not, discobot.py is called.


created mostly by following tutorials here: https://makerhacks.com/python-messages-discord/
