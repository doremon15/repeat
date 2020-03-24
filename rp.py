import discord
from discoird.ext import commands

TOKEN = 'NjMxNzQ3ODgyODA2MTQ5MTMw.XnnMwg.ZPJd7uetoaFMg7kMW2nk-WhIsus'

client = commands.Bot(command_prefix ='+')

@client.event
async def on_ready():
    print('Bot is ready.')
    
@client.command()
async def 1():
  await client.say('1\1\1\1\1\1\1cnf')
  
  client.run(TOKEN)
