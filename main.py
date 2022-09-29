import config
import discord
from discord.ext import commands

TOKEN = config.discord_bot_token

intents = discord.Intents.all()


client = commands.Bot(command_prefix = '.', intents = intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user} ')

@client.command()
async def ping(ctx): 
    await ctx.send('pong!')

@client.command()
async def endgame(ctx):
    await ctx.send('Game is finnito time for me to log out')


client.run(TOKEN)


