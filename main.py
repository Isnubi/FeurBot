from private.config import token  # get token

# import discord bot libraries
from discord.ext import commands
import discord
import asyncio
import random

# activate intents and set bot prefix to "!"
intents = discord.Intents.default()
intents.presences = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

# remove help command to use the custom one
bot.remove_command('help')


async def status_task():
    activity = [
        discord.Activity(
            type=discord.ActivityType.playing,
            name='FeurGame'
        ),
        discord.Activity(
            type=discord.ActivityType.listening,
            name='FeurMusic'
        ),
        discord.Activity(
            type=discord.ActivityType.watching,
            name='FeurMovie'
        ),
        discord.Activity(
            type=discord.ActivityType.listening,
            name='on {0} servers'.format(len(bot.guilds))
        ),
        discord.Activity(
            type=discord.ActivityType.watching,
            name='on {0} users'.format(len(set(bot.get_all_members())))
        ),
        discord.Activity(
            type=discord.ActivityType.playing,
            name='Get commands with !help'
        )
    ]  # list of bot activities
    i = 0
    while True:
        await bot.change_presence(activity=activity[i])
        i += 1
        if i > (len(activity) - 1):
            i = 0
        await asyncio.sleep(60)


@bot.event
async def on_ready():
    print('Bot ready!')
    bot.loop.create_task(status_task())


bot.load_extension("cogs.Temp")
bot.load_extension("cogs.CPU")
bot.load_extension("cogs.RAM")
bot.load_extension("cogs.Purge")
bot.load_extension("cogs.QuoiFeur")
bot.load_extension("cogs.PFP")
bot.load_extension("cogs.Say")
bot.load_extension("cogs.Help")
bot.load_extension("cogs.Ping")
bot.load_extension("cogs.CommandLog")
bot.load_extension("cogs.Roll")
bot.load_extension("cogs.UserInfo")
bot.load_extension("cogs.ServerInfo")
bot.load_extension("cogs.PlaySound")
bot.load_extension("cogs.CogsManagement")
bot.load_extension("cogs.MemberJoinLeave")

bot.run(token)
