import config
import discord
from discord.ext import commands
import json
import os

current_directory = os.getcwd()
os.chdir(current_directory)

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

@client.command()
async def setup(ctx):
    await create_account_for_all_users()

async def create_account_for_all_users():
    with open("balances.json", "r") as file: 
        current_users = json.load(file)
    # print(current_users)
    for user in client.users:
        if(str(user.id) not in current_users):
            current_users[str(user.id)] = {}
            current_users[str(user.id)]["balance"] = 1000
            current_users[str(user.id)]["current_profits"] = 0 
            current_users[str(user.id)]["current_losses"] = 0
            current_users[str(user.id)]["user_name"] = user.name
    
    print(current_users)
    with open("balances.json", "w") as file:
        json.dump(current_users,file)

@client.command()
async def balance(ctx):
    if(account_exists(ctx.author) == False):
        await ctx.send("You don't have an account yet. To make one use the .create-account command") 
    else: 
        await ctx.send("u broke bitch u got this much left " + await get_balance(ctx.author))

def account_exists(user): 
    with open("balances.json", "r") as file:
        current_users = json.load(file)
    
    if(str(user.id) in current_users):
        return True
    else:
        return False

async def get_balance(user):
    with open("balances.json", "r") as file: 
        current_users = json.load(file)
    
    wanted_user = current_users[str(user.id)]
    return str(wanted_user)



client.run(TOKEN)


