#To ensure this script keeps running, add the following line to cron
#*/1 * * * * ps aux|grep -v grep|grep discoMotion.py || nohup sudo python3.x /home/pi/discords/discoMotion.py &
#HOW IT WORKS: once a minute cron will check to see if script is running, and if not starts it

import os
import sys
import subprocess
import glob
import time
import discord

# discord client
client = discord.Client()

# create a new event
@client.event
async def on_ready():
     print("(Disco Motion Initiated)")
     #this next bit doesn't seem to work but doesn't throw an error 
     client.send_message(client.get_channel('DISC-CHANNEL-ID'), 'Disco Motion Initiated') 

# listen for specific messages
@client.event
async def on_message(message):
    if message.content.startswith("/help"):
        await client.send_message(message.channel, "You can: \n" + "/help for this menu\n" + "/lastvid for last caputured video\n" + "/lastpic for last captured image")
    if message.content.startswith("/lastvid"):
        await client.send_message(message.channel, "sending last video");
        list_of_vids = glob.glob('/path/to/videos/*.avi');
        time.sleep(3)
        await client.send_file(message.channel, max(list_of_vids, key=os.path.getctime))
    if message.content.startswith("/lastpic"):
        await client.send_message(message.channel, "sending last picture");
        list_of_pics = glob.glob('/path/to/images/*.jpg');
        time.sleep(3)
        await client.send_file(message.channel, max(list_of_pics, key=os.path.getctime))

# run the bot
bot = "BOT-TOKEN-GOES-HERE"
client.run(bot)
