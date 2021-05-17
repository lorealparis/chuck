import discord
from discord.client import Client
from discord.flags import Intents
from dotenv import load_dotenv
import os
import aiohttp
from discord.ext import commands
import random

chucknorris_random_api = "https://api.chucknorris.io/jokes/random"
chucknorris_search_api = "https://api.chucknorris.io/jokes/search?query="

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
print(os.getenv("USERNAME"))
intents=discord.Intents.default()
intents.members=True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Ready!")


@client.event
async def on_message(message):
    if message.author ==client.user:
        return
    if message.content.startswith("!random"):
        async with aiohttp.ClientSession() as session:
            async with session.get(chucknorris_random_api) as response:
                if response.status == 200:
                    js = await response.json()
                    await message.channel.send (js ["value"])
        return

    if message.content.startswith("!search"):
        search_term = message.content[8:]
        async with aiohttp.ClientSession() as session:
            async with session.get(chucknorris_search_api+search_term) as response:
                if response.status == 200:
                    js = await response.json()
                    await message.channel.send (random.choice(js["result"])["value"])
        return


   


client.run(TOKEN)


