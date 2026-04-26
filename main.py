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
channel_id = config.get('channel_id')
if channel_id is not None:
    channel_id = int(channel_id)
cooldown_minutes = config.get('cooldown_minutes', 150)
app_commands = None
last_fetch_time = 0
fetch_interval = 5
prefix = config.get('prefix', '!')
bot = commands.Bot(command_prefix=prefix, self_bot=True)

@tasks.loop(seconds= 5)
async def beg_task():
    global app_commands, last_fetch_time
    try:
        channel = bot.get_channel(channel_id)
        if channel and isinstance(channel, discord.TextChannel):
            current_time = asyncio.get_event_loop().time()
            if not app_commands or current_time - last_fetch_time > fetch_interval:
                app_commands = await channel.application_commands()
                last_fetch_time = current_time

            if app_commands:
                beg_command = next((cmd for cmd in app_commands if cmd.name == "bump"), None)
                if beg_command:
                    try:
                        await beg_command(channel)
                        print("Bump has been successful.")
                        beg_task.change_interval(minutes=cooldown_minutes)
                        return
                    except Exception as inner_e:
                        print(f"Error executing /bump command: {inner_e}")
                else:
                    print("'/bump' command not found in the channel.")
    except discord.HTTPException as e:
        if e.status == 429:
            print("Rate limited. Waiting...")
            await asyncio.sleep(e.retry_after)
        else:
            print(f"HTTPException in beg_task: {e}")
    except Exception as e:
        print(f"Error in beg_task: {e}")

@bot.event
async def on_ready():
    print("=============================================")
    print(f"Logged in as {bot.user.name} ({bot.user.id})")
    print("============================================= \n")
    beg_task.start()

bot.run(token)
