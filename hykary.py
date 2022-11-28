# MUT
import hikari
from json import loads
from pathlib import Path
import lightbulb

# DEF CON 01


config = loads(Path("config.json").read_text())
bot = lightbulb.BotApp(
    token=config["token"],
    )


bot.run()
