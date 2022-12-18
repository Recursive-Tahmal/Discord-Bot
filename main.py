import discord  # libary that calls discord
from json import loads
from pathlib import Path

# ===========================================================#

config = loads(Path("config.json").read_text())

# mandatory shit.... new API... OLD CUM
intents = discord.Intents.all()
bot = discord.Client(intents=intents)
intents.message_content = True
intents.members = True
# CONFIOG FILE SO THAT DOES NOT SENT TO GITHUB
token = config["token"]


# LOGS THAT BOT IS OK
@bot.event
async def on_ready():
    print("BOT IS OPERATIONAL")


@bot.event  # replies to the message with a verry calm awnser
async def on_message(msg):
    username = msg.author.display_name
    if msg.author == bot.user:
        return
    if msg.content == "hello":
        await msg.channel.send(f"FUCK OFF " + username)

@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    if msg.content == 'darkspook':
        await msg.channel.send('Ratem')


@bot.event  # sends a greeting cart for the player NOT WORKING
async def on_join(member):
    guild = member.guild
    guildname = guild.name
    dmchannel = await member.create_dm()
    await dmchannel.send(f'GREETINGS FROM {guildname}')
    print("NEW USER")


#@bot.event
#async def on_raw_reaction_add(payload):



# ====================#
#        RUN         #
# ====================#
bot.run(token)
