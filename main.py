from private.config import token # get token

# import libraries
import random
import re
import subprocess
import psutil
# import discord bot libraries
from discord.ext import commands
import discord


# set box prefix to "!"
bot = commands.Bot(command_prefix='!')


# alert in the console when bot is ready
@bot.event
async def on_ready():
    print('Bot ready!')


# command to check bot delay
@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}s of delay'.format(round(bot.latency, 1)))


bot.load_extension("cogs.Temp")
bot.load_extension("cogs.CPU")
bot.load_extension("cogs.RAM")
bot.load_extension("cogs.Purge")
bot.load_extension("cogs.QuoiFeur")


bot.run(token)
