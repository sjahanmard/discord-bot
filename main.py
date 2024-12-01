import discord
import os
from all_options import AllOptions
from utils import load_config
import time

load_config()

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True  

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'I love Sobhan!')

@client.event
async def on_guild_channel_create(channel):
    time.sleep(1)
    if isinstance(channel, discord.TextChannel) and channel.name.startswith("ticket"):
        view = AllOptions()  
        await channel.send("Hello! Please choose of the the options below?", view=view)

client.run(os.getenv("TOKEN"))
