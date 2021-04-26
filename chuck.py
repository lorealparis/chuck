import discord
from discord.client import Client
from discord.flags import Intents
from dotenv import load_dotenv
import os
import aiohttp
from discord.ext import commands

chucknorris_api = "https://api.chucknorris.io/jokes/random"
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = int(os.getenv("DISCORD_GUILD"))
print(os.getenv("USERNAME"))
intents=discord.Intents.default()
intents.members=True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Ready!")
    for guild in client.guilds:
        if guild.id == GUILD:
            for member in guild.members:
                print (member.name)
            break

@client.event
async def on_message(message):
    if message.author ==client.user:
        return
    if message.content.startswith("!random"):
        async with aiohttp.ClientSession() as session:
            async with session.get(chucknorris_api) as response:
                if response.status == 200:
                    js = await response.json()
                    await message.channel.send (js ["value"])


   


client.run(TOKEN)


