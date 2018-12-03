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
    if message.content.startswith("/helpme"):
        await client.send_message(message.channel, "Need help? Try /uptime for time since reboot, /reboot for time until reboot, and /helpme to see this message.")
    if message.content.startswith("/uptime"):
        result = subprocess.check_output(['/home/pi/bin/mud/mudup.sh'])
    if message.content.startswith("/reboot"):
        result = subprocess.check_output(['/home/pi/bin/mud/mudbc.sh'])

# run the bot
bot = "BOT-TOKEN-GOES-HERE"
client.run(bot)
