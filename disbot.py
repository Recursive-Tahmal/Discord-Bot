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


bot.run()
