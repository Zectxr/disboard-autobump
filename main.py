import sys
sys.path.insert(0, 'discord.py-self-master')
import asyncio
import discord
from discord.ext import commands, tasks
import json

def load_config(file_path):
    with open(file_path, encoding='utf-8') as f:
        return json.load(f)

config = load_config('config/config.json')
token = config.get('token')
prefix = config.get('prefix', '!')

bot = commands.Bot(command_prefix=prefix, self_bot=True)



@bot.event
async def on_ready():
    print("=============================================")
    print(f"Logged in as {bot.user.name} ({bot.user.id})")
    print("============================================= \n")

bot.run(token)
