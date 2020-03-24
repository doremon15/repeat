import discord
from discord.ext import commands
import asynico
import time

TOKEN = 'NjkxOTY4NzYzNTY5ODk3NTIy.XnnsLA.ZZIh7275cX2AOt-Kg24PL5YZF-U'

client = commands.Bot(command_prefix ='+')

@client.event
async def on_ready():
    print('Bot is ready.')
    
@client.command()
async def +1():
  await client.say('1\1\1\1\1\1\1cnf')
  
client.run(TOKEN)
