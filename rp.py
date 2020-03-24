import discord
from discord.ext import commands

TOKEN = 'NjkxOTM1OTAzODkxMDYyNzk1.XnnNng.NRw1vwC90Hdr6rgP4TXlKEp8Whw'

client = commands.Bot(command_prefix ='+')

@client.event
async def on_ready():
    print('Bot is ready.')
    
@client.command()
async def 1():
  await client.say('1\1\1\1\1\1\1cnf')
  
  client.run(TOKEN)
