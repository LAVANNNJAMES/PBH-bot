import discord
from discord.ext import commands

TOKEN = 'MTAyMzYxNjk4NzU0NjUyNTc5OA.GqzLli.abmHbbX5inrsi1LN745Zrf0E0VJPY9h45Yp4Q4'

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
    client.logout()


client.run(TOKEN)


