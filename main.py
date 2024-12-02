import discord
import os
from components.all_options import AllOptions
from utils import load_config
import time
from utils.service_account_key import service_account_key
from datetime import datetime
from utils.handle_cancellation import handle_cancellation

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


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!cancel:"):
        try:
            cancel_id = message.content.split(":", 1)[1].strip()
            is_cancelled = handle_cancellation(id=cancel_id)
            if is_cancelled:
                await message.channel.send(f"Cancelled order id {cancel_id}." )
        except IndexError:
            await message.channel.send("Invalid usage of `!cancel`. Please provide an ID, e.g., `!cancel:12345`.")

token = os.getenv("TOKEN")
if not token:
    print("Token is missing!")
else:
    print("Token seems set!")
    client.run(os.getenv("TOKEN"))
