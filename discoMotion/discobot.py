import os
import sys
import time
import glob
import discord
import subprocess

# discord client
client = discord.Client()

def process_message(message):
    args = message.content.split(" ")

    return args

# create a new event
@client.event
async def on_ready():
     print("BOOP BEEP BOOP SQUEEE! (Bot Ready)")

# listen for specific messages
@client.event
async def on_message(message):
    if message.content.startswith("/?"):
        await client.send_message(message.channel, "Available Commands: /?, /lpic, /lvid, /mstart, /mstop, /still (no stills while motion is running)")
    if message.content.startswith("/still"):
        result = subprocess.check_output(['/home/USER/bin/still.sh']);
        still = glob.glob('/home/USER/bin/stills/discorequest.jpg');
        await client.send_file(message.channel, max(still, key=os.path.getctime))
    if message.content.startswith("/lpic"):
        #await client.send_message(message.channel, "sending last picture");
        list_of_pics = glob.glob('/home/USER/bin/motion/*.jpg');
        time.sleep(10)
        await client.send_file(message.channel, max(list_of_pics, key=os.path.getctime))
    if message.content.startswith("/lvid"):
        #await client.send_message(message.channel, "sending last video");
        list_of_vids = glob.glob('/home/USER/bin/motion/*.avi');
        time.sleep(3)
        await client.send_file(message.channel, max(list_of_vids, key=os.path.getctime))
    if message.content.startswith("/mstop"):
        result = subprocess.check_output(['/home/USER/bin/motionkill']);
        await client.send_message(message.channel, "Motion has been disabled.")
    if message.content.startswith("/mstart"):
        result = subprocess.check_output(['/home/USER/bin/motionrev']);
        await client.send_message(message.channel, "Motion has been enabled.")

# run the bot
bot = "TOKEN"
client.run(bot)
