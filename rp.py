import discord
from discoird.ext import commands

TOKEN = ''

client = commands.Bot(command_prefix ='NjMxNzQ3ODgyODA2MTQ5MTMw.XnnLYA.XTZGTUtptxhjQ9kq3mnaHjZNUMs')

@client.event
async def on_ready():
    print('Bot is ready.')
    
@client.command()
async def 1():
  await client.say('1\1\1\1\1\1\1cnf')
  
  client.run(TOKEN)
