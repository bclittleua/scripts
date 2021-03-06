# NOTE1: discord lib requires at least python3.6 to function 
# NOTE2: This script will crash if you briefly/periodically lose internet connectivity, to fix
# you need to add the following line to sudo crontab (not user cron) to keep the bot running
# */1 * * * * ps aux|grep -v grep|grep discobot.py||nohup sudo python3.6 /home/pi/bin/discords/discobot.py &
# Every minute look for discobot.py and IF NOT FOUND, run dicscobot. 
# NOTE3: If run as user vs. root (cron vs. sudo cron) the 
# sort method will not work and create multiple instances!

import discord
import sys
import os
import subprocess

# discord client
client = discord.Client()

# create a new event
@client.event
async def on_ready():
     print("BOOP BEEP BOOP SQUEEE! (Bot Ready)")

# listen for specific messages
@client.event
async def on_message(message):
    if message.content.startswith("/panic"):
        await client.send_message(message.channel, "Need help? Try:\n"+"/uptime for time since reboot\n"+"/reboot for time until reboot and\n"+"/panic to see this message.")
    if message.content.startswith("/uptime"):
        # runs an offline script to calculate time since boot, then writes value to file
        # after script runs, send a canned message to channel and append the above value
        result = subprocess.check_output(['/home/pi/bin/mud/mudup.sh']);
        await client.send_message(message.channel, "The MUD has been up for " + open('/home/pi/bin/mud/sw-up.log').read())  
    if message.content.startswith("/reboot"):
        result = subprocess.check_output(['/home/pi/bin/mud/mudbc.sh']);
        await client.send_message(message.channel, "The MUD will restart in " + open('/home/pi/bin/mud/sw-up.log').read())  

# run the bot using the tokenID you create at https://discordapp.com/developers/applications/
bot = "53CR3T-130T-T0K3N-G035-H3R3"
client.run(bot)
