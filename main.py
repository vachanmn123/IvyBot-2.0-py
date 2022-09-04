from cProfile import label
from datetime import datetime
import encodings
from multiprocessing.connection import wait
from os import sync
import os
from unicodedata import name
from disnake import Intents
import disnake
from disnake.ext import commands
import json
import logging

# Setup bot client
intents = disnake.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix=json.load(open("config.json"))["bot_prefix"],
    intents=intents,
    test_guilds=json.load(open("config.json"))["test_guilds"],
    help_command=None,
)

# Setup logging
logger = logging.getLogger("disnake")
if json.load(open("config.json"))["development"]:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)
handler = logging.FileHandler(
    filename=f"logs/IvyBot-{datetime.now().isoformat()}.log",
    encoding="utf-8",
    mode="w",
)
consoleHandler = logging.StreamHandler()
handler.setFormatter(
    logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
)
consoleHandler.setFormatter(
    logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
)
logger.addHandler(handler)
logger.addHandler(consoleHandler)
bot.logger = logger


@bot.event
async def on_ready():
    """prints bot is running"""
    bot.logger.info(f"Logged in as {bot.user.name}({bot.user.id})")
    activity = disnake.Activity(
        type=disnake.ActivityType.watching,
        name=f"{len(bot.guilds)} servers",
    )
    await bot.change_presence(activity=activity)


@bot.command()
async def help(ctx):
    return await ctx.reply("Press `/` on your keyboard to see a list of commands.")


# Load cogs
bot.logger.info("Loading cogs")
for file in os.listdir("cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")
bot.logger.info("Cogs loaded")

# Run bot
bot.run(json.load(open("config.json"))["bot_token"])
