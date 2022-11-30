# MUT
import hikari
from json import loads
from pathlib import Path
import lightbulb

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
    await ctx.respond('PING = Shows you pong')

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


#MATH.... not drugs
@bot.command
@lightbulb.option('num1', 'the First number', type=int)
@lightbulb.option('num2', 'the second number', type=int)
@lightbulb.command('add', 'MAKES MATH FOR YOU FUCKING KUNT')
@lightbulb.implements(lightbulb.SlashCommand)
async def add (ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)


bot.run()
