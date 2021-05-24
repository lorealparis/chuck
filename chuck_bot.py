import discord
from discord.client import Client
from discord.flags import Intents
from dotenv import load_dotenv
import os
import aiohttp
from discord.ext import commands
import random as rnd
from discord.ext import commands

chucknorris_random_api = "https://api.chucknorris.io/jokes/random"
chucknorris_search_api = "https://api.chucknorris.io/jokes/search?query="

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
print(os.getenv("USERNAME"))
intents=discord.Intents.default()
intents.members=True

bot = commands.Bot(command_prefix="!")

@bot.command()
async def ready(ctx):
    print("Ready!")


@bot.command()
async def random(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(chucknorris_random_api) as response:
            if response.status == 200:
                js = await response.json()
                await ctx.channel.send (js ["value"])
    return

@bot.command()
async def search(ctx,search_term):
    async with aiohttp.ClientSession() as session:
        async with session.get(chucknorris_search_api+search_term) as response:
            if response.status == 200:
                js = await response.json()
                await ctx.channel.send (rnd.choice(js["result"])["value"])
    return


   


bot.run(TOKEN)
