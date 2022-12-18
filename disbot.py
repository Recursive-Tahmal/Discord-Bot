# MUT
import time
import hikari
from json import loads
from pathlib import Path
import pyjokes
import wikipedia
import lightbulb
import jaconv
from biblehub import search as b_search

# DEF CON 01

# NO TOUCHY
config = loads(Path("config.json").read_text())
bot = lightbulb.BotApp(
    token=config["token"],
    #default_enabled_guilds=(1045906948341633115)
)


# NO TOUCHY

@bot.listen(hikari.StartedEvent)
async def bot_start(event):
    print('IM ALIVE')

@bot.command
@lightbulb.command('help', 'Help for the needed')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping (ctx):
    await ctx.respond(HELP_MESSAGE)

@bot.command
@lightbulb.option('text', 'The Text you want to convert')
@lightbulb.command('japan', 'Transform your text to Katakana')
@lightbulb.implements(lightbulb.SlashCommand)
async def japan (ctx: lightbulb.Context):
    texto = ctx.options.text
    await ctx.respond(jaconv.alphabet2kata(texto))

#jokes NOT FUNNY!!!!
@bot.command
@lightbulb.command('nerd_joke', 'Random Programmer Joke of the mind')
@lightbulb.implements(lightbulb.SlashCommand)
async def joke (ctx):
    await ctx.respond(pyjokes.get_joke())

#GROUP AND CHILDS
@bot.command
@lightbulb.command('group', 'group test')
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
@lightbulb.option('text', 'the text to search')
@lightbulb.command('search', 'Search for something in Wikipedia')
@lightbulb.implements(lightbulb.SlashCommand)
async def wiki (ctx: lightbulb.Context):
    try:
        await ctx.respond(wikipedia.summary(ctx.options.text))
    except:
        await ctx.respond("Not found")


#random WIKI WORKS
@bot.command
@lightbulb.command('randomfact', 'Gets a random fact fro the web, not responsible from bad search!!!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ranwiki (ctx: lightbulb.Context):
    randomwiki = wikipedia.random(1)
    print(randomwiki)
    resposta = wikipedia.summary(randomwiki, 6)
    print(resposta)
    await ctx.respond(randomwiki)
    await ctx.respond(resposta)


#MATH.... not drugs
@bot.command
@lightbulb.option('num1', 'the first number', type=float)
@lightbulb.option('num2', 'the second number', type=float)
@lightbulb.command('add', 'MAKES MATH FOR YOU FUCKING KUNT')
@lightbulb.implements(lightbulb.SlashCommand)
async def add (ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)

#subtract
@bot.command
@lightbulb.option('num1', 'the first number', type=float)
@lightbulb.option('num2', 'the second number', type=float)
@lightbulb.command('subtract', 'MAKES MATH FOR YOU FUCKING KUNT')
@lightbulb.implements(lightbulb.SlashCommand)
async def add (ctx):
    await ctx.respond(ctx.options.num1 - ctx.options.num2)

#divide
@bot.command
@lightbulb.option('num2', 'second number', type=float)
@lightbulb.option('num1', 'first number', type=float)
@lightbulb.command('divide', 'MAKES MATH FOR YOU FUCKING KUNT')
@lightbulb.implements(lightbulb.SlashCommand)
async def add (ctx):
    if(ctx.options.num2 == 0):
        await ctx.respond("Error! cannot divide by zero")
    else:
        await ctx.respond(ctx.options.num1 / ctx.options.num2)

#multiply
@bot.command
@lightbulb.option('num1', 'the first number', type=float)
@lightbulb.option('num2', 'the second number', type=float)
@lightbulb.command('multiply', 'MAKES MATH FOR YOU FUCKING KUNT')
@lightbulb.implements(lightbulb.SlashCommand)
async def add (ctx):
    await ctx.respond(ctx.options.num2 * ctx.options.num1)

############################################################################
HELP_MESSAGE = """
Commands Available:
`add` - makes a math addition
`search` - search the web for the context
`joke` - does not make you laugh
"""



bot.run()
