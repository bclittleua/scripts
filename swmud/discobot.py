import discord
import sys
import os
import subprocess

# discord client
client = discord.Client()

# create a new event
@client.event
async def on_ready():
     print("BOOP BEEP BOOP SQUEEE!")
     print("(Bot Ready)")

# listen for specific messages
@client.event
async def on_message(message):
    if message.content.startswith("/helpme"):
        await client.send_message(message.channel, "Hey there. /uptime for time to reboot. /helpme to see this message.")


    if message.content.startswith("/uptime"):
        result = subprocess.check_output(['/home/pi/bin/man/manbc.sh'])
        #await client.send_message(message.channel, "Stand by.")

# run the bot
bot = "YOUR_DISCORD_BOT_TOKEN_GOES_HERE"
client.run(bot)
