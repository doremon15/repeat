import discord
from discord.ext import commands

TOKEN = 'NjkxOTM1OTAzODkxMDYyNzk1.XnnPbA.CCbL72vOZApf7J9hvARomFlqzjI'

client = commands.Bot(command_prefix ='+')

@client.event
async def on_ready():
    print('Bot is ready.')
    
@client.command()
async def 1():
  await client.say('1\1\1\1\1\1\1cnf')
  
  client.run(TOKEN)
