import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

Client = discord.Client()
bot = commands.Bot(command_prefix = "+")

@bot.event
async def on_ready():
    print("Commands system ready for Bot!")
    await bot.change_presence(game=discord.Game(name='+help'))

@bot.event
async def on_message(message):
    if message.content.upper().startswith("+RATE"):
        print("Received Command +rate")
        print("rating player")
        for i in range(1):
            rating = random.randint(1,100)
            ratedUser = message.content.split(" ")
            await bot.send_message(message.channel, "I'd rate %s %d / 100" % (" ".join(ratedUser[1:]),rating))
            

bot.run("NDAzMTg1MjUwMzg3MjMwNzIx.DUJ-fA.Bgi13DRka-o_RY2Vw1Jjrh0v4AA")
