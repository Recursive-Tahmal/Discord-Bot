import discord  # libary that calls discord
from json import loads
from pathlib import Path
#===========================================================#

config = loads(Path("config.json").read_text())

#mandatory shit.... new API... OLD CUM
intents = discord.Intents.default()
intents.message_content = True
# CONFIOG FILE SO THAT DOES NOT SENT TO GITHUB
token = config["token"]





#LOGS THAT BOT IS OK
bot = discord.Client(intents=intents)
@bot.event
async def on_ready():
    print("BOT IS OPERATIONAL")

@bot.event #replies to the message with a verry calm awnser
async def on_message(msg):
    username = msg.author.display_name
    if msg.author == bot.user:
        return
    if msg.content == "hello":
        await msg.channel.send("FUCK OFF " + username)

@bot.event
async def on_join(member):

bot.run(token)