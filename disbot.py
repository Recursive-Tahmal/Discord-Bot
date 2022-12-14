# MUT
import time
import hikari
from json import loads
from pathlib import Path
import pyjokes
import wikipedia
import lightbulb
from googlesearch.googlesearch import GoogleSearch


# DEF CON 01

# NO TOUCHY
config = loads(Path("config.json").read_text())
bot = lightbulb.BotApp(
    token=config["token"],
    default_enabled_guilds=(1045906948341633115)
)


# NO TOUCHY

@bot.listen(hikari.StartedEvent)
async def bot_start(event):
    print ('IM ALIVE')

@bot.command
@lightbulb.command('ping', 'TELLS YOU THE NAME OF A XINESE EMPEROR')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping (ctx):
    await ctx.respond('XING XONG')

@bot.command
@lightbulb.command('help', 'Inform you what are the commands of the bot')
@lightbulb.implements(lightbulb.SlashCommand)
async def help (ctx):
    await ctx.respond(HELP_MESSAGE)
    print('XING XONG')

#jokes NOT FUNNY!!!!
@bot.command
@lightbulb.command('joke', 'Random Joke of the mind')
@lightbulb.implements(lightbulb.SlashCommand)
async def joke (ctx):
    await ctx.respond(pyjokes.get_joke())

#GROUP AND CHILDS
@bot.command
@lightbulb.command('group', 'groupo test')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group (ctx):
    pass

#child 1
@my_group.child
@lightbulb.command('subcommand', 'this is a subcommand')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('i am a sub command')
#child 2
@my_group.child
@lightbulb.command('subcommand2', 'this is a subcommand2')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('i am a sub command2')

#wikipedia1 search generic
@bot.command
@lightbulb.option('long', 'How long should the text be?', type=int)
@lightbulb.option('text', 'the text to search')
@lightbulb.command('search', 'Your search question')
@lightbulb.implements(lightbulb.SlashCommand)
async def wiki (ctx: lightbulb.Context):
    resposta = ctx.options.text
    pesado = ctx.options.long
    await ctx.respond(wikipedia.summary(resposta, pesado))
#random WIKI NOT WORKING
@bot.command
@lightbulb.command('randomfact', 'Gets a random fact fro the web, not responsable from bad search!!!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ranwiki (ctx: lightbulb.Context):
    randomwiki = wikipedia.random(1)
    print(randomwiki)
    resposta = wikipedia.summary(randomwiki,6)
    print(resposta)
    await ctx.respond(randomwiki)

#MATH.... not drugs
@bot.command
@lightbulb.option('num1', 'the First number', type=int)
@lightbulb.option('num2', 'the second number', type=int)
@lightbulb.command('add', 'MAKES MATH FOR YOU FUCKING KUNT')
@lightbulb.implements(lightbulb.SlashCommand)
async def add (ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)
    print('MATH')



############################################################################
HELP_MESSAGE = """
Commands Available:
`add` - makes a math addition
`search` - search the web for the context
`joke` - does not make you laught
"""



bot.run()
