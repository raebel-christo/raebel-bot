#403185250387230721
#NDAzMTg1MjUwMzg3MjMwNzIx.DUJ-fA.Bgi13DRka-o_RY2Vw1Jjrh0v4AA

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
    await bot.change_presence(game=discord.Game(name='+help'))
    print("Bot is now online!")

@bot.event
async def on_message(message):
    SenderID = message.author.id
    Greetings = ("HI","HELLO","HEY","HOI","HALLO","HAI","HULLO","SUP","HOLA")
    Wassup = ["WHAT'S UP","WHATS UP","WHAT'S UP?","WHATS UP?","WASSUP","WASSUP?"]
    if message.author.id != "403185250387230721":
        words = message.content.upper().split(" ")
        for i in words:
            for x in Greetings:
                if x == i:
                    await bot.send_message(message.channel, "Hey there, <@%s>" % (SenderID))
                    print("Replied Hi")
        for i in Wassup:
            if i in " ".join(words):
                await bot.send_message(message.channel, "The ceiling is up, <@%s>" % (SenderID))

bot.run("NDAzMTg1MjUwMzg3MjMwNzIx.DUJ-fA.Bgi13DRka-o_RY2Vw1Jjrh0v4AA")
