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

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)


bot.run()
