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



bot.run()
