import sys
sys.path.insert(0, 'discord.py-self-master')
import asyncio
import discord
from discord.ext import commands, tasks
import json

def read_config(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)

# Load startup settings from JSON
settings = read_config('config/config.json')
token = settings.get('token')
target_channel_id = settings.get('channel_id')
if target_channel_id is not None:
    target_channel_id = int(target_channel_id)

cooldown = settings.get('cooldown')
refresh_interval = 5
cached_commands = None
last_refresh_time = 0
command_prefix = settings.get('command_prefix', '!')
bot = commands.Bot(command_prefix=command_prefix, self_bot=True)

@tasks.loop(seconds=refresh_interval)
async def bump_loop():
    global cached_commands, last_refresh_time
    try:
        channel = bot.get_channel(target_channel_id)
        if not channel or not isinstance(channel, discord.TextChannel):
            return

        now = asyncio.get_event_loop().time()
        if not cached_commands or now - last_refresh_time > refresh_interval:
            cached_commands = await channel.application_commands()
            last_refresh_time = now

        if not cached_commands:
            return

        bump_command = next((cmd for cmd in cached_commands if cmd.name == 'bump'), None)
        if not bump_command:
            print("'/bump' command not found in the channel.")
            return

        try:
            await bump_command(channel)
            print('Bump was successful.')
            bump_loop.change_interval(seconds=cooldown)
            return
        except Exception as command_error:
            print(f"Error executing /bump command: {command_error}")

    except discord.HTTPException as http_error:
        if http_error.status == 429:
            print('Rate limited. Waiting...')
            await asyncio.sleep(http_error.retry_after)
        else:
            print(f"HTTP error in bump_loop: {http_error}")
    except Exception as error:
        print(f"Error in bump_loop: {error}")

@bot.event
async def on_ready():
    # Start the bump loop once the bot is ready and logged in
    print('=' * 45)
    print(f"Logged in as {bot.user.name} ({bot.user.id})")
    print('=' * 45)
    bump_loop.start()

bot.run(token)