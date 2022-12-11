import hikari
import lightbulb
import requests
import datetime
from json import loads
from pathlib import Path

# python -m venv env

# orders matter for dicorators

# bot token
config = loads(Path("config.json").read_text())
bot = lightbulb.BotApp(
    token=config["token"],
)


# @bot.listen(hikari.GuildMessageCreateEvent)  # listens and prints on the console what's being typed
# async def print_message(event):
#     print(event.content)


@bot.listen(hikari.StartedEvent)  # console types bot has started
async def bot_started(event):
    print("Bot has started!")


@bot.command
@lightbulb.command("ping", "Says pong!")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):  # say ping and respond to pong
    await ctx.respond("Pong!")


# grouping commands
@bot.command
@lightbulb.command("group", "This is a group")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(ctx):
    pass


@my_group.child
@lightbulb.command("subcommand", "This is a subcommand")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond("I am a subcommand!")


# this will add 2 numbers
@bot.command
@lightbulb.option("num2", "The second number", type=float)  # options
@lightbulb.option("num1", "The first number", type=float)
@lightbulb.command("add", "Add two numbers together")
@lightbulb.implements(lightbulb.SlashCommand)
async def addnums(ctx):
    await ctx.respond(ctx.options.num2 + ctx.options.num1)


# API test
@bot.command
@lightbulb.command("joke", "tells a joke")
@lightbulb.implements(lightbulb.SlashCommand)
async def jokes(ctx):
    response = requests.get("https://api.chucknorris.io/jokes/random")
    fox = response.json()
    await ctx.respond(fox["value"])


@bot.command
@lightbulb.command("cat", "sends a cat picture")
@lightbulb.implements(lightbulb.SlashCommand)
async def cat(ctx):
    response = requests.get("https://aws.random.cat/meow")
    cat = response.json()["file"]
    await ctx.respond(cat)


# calculates how much left for the given time
@bot.command
@lightbulb.option("year", "Enter the year", type=int)
@lightbulb.option("month", "Enter the month", type=int)
@lightbulb.option("day", "Enter the day", type=int)
@lightbulb.command("date", "tells how long till the given date")
@lightbulb.implements(lightbulb.SlashCommand)
async def date(ctx):
    present = datetime.datetime.now()
    given_date = datetime.datetime(ctx.options.year, ctx.options.month, ctx.options.day, 0, 0, 0)
    await ctx.respond(given_date - present)


# TODO Make a command that tells people what's trending upon your friends -Example Minecraft server ip 192.168.1.1


#---------------------------MAIN------------------------------------#
bot.run()