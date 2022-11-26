import discord  # libary that calls discord
from json import loads
from pathlib import Path
#===========================================================#

config = loads(Path("config.json").read_text())

#mandatory shit.... new API... NEW CUM
intents = discord.Intents.default()
intents.message_content = True
#
token = config["token"]

bot = discord.Client(intents=intents)
@bot.event
async def on_ready():
    print("BOT IS OPERATIONAL")


bot.run(token)