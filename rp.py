import discord
from discord.ext import commands
import asynico
import time

TOKEN = 'NjkxOTY4NzYzNTY5ODk3NTIy.XnnsLA.ZZIh7275cX2AOt-Kg24PL5YZF-U'

client = discord.Client()

@client.event
async def on_message(message):
    print(message.content) # Now every message sent will be printed to the console

@client.event
async def on_message(message):
    if message.content.find("1") != -1:
        await message.channel.send("1\1\1\1") # If the user says !hello we will send back hi
  
client.run(TOKEN)
