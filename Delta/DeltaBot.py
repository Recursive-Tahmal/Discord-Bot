import lightbulb
import hikari
from riotwatcher import LolWatcher
import json
import pathlib

config = json.loads(pathlib.Path("config.json").read_text())
bot = lightbulb.BotApp(
    token=config["token"][0],
)


@bot.listen(hikari.StartedEvent)
async def bot_start(event):
    print('IM ALIVE')


@bot.command
@lightbulb.option("name", "Enter your summoner's name", type=str)
# TODO validation
@lightbulb.option("server", "Enter the server", type=str, choices=["Europe Nordic & East", "Europe West", "North America", "Korea", "Brazil", "Latin America North", "Latin America South", "Oceania", "Russia", "Turkey"])
@lightbulb.command('rank', 'Find the giving name rank')
@lightbulb.implements(lightbulb.SlashCommand)
async def rank(ctx):
    # Riot stuff
    watcher = LolWatcher(config["token"][1])
    REGION_CODES = {
        "Europe Nordic & East": "EUN1",
        "Europe West": "EUW1",
        "North America": "NA1",
        "Korea": "KR",
        "Brazil": "BR1",
        "Latin America North": "LA1",
        "Latin America South": "LA2",
        "Oceania": "OC1",
        "Russia": "RU",
        "Turkey": "TR1"
    }
    me = watcher.summoner.by_name(
        REGION_CODES[ctx.options.server], ctx.options.name)
    rank = watcher.league.by_summoner(
        REGION_CODES[ctx.options.server], me["id"])
    if rank == []:
        await ctx.respond("Unranked")
    else:
        # print all tiers in different dictionaries
        x = ""
        for i in rank:
            x += f"{i['queueType']} {i['tier']} {i['rank']} {i['leaguePoints']}LP\n"
        await ctx.respond(x)


bot.run()
