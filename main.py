from private.config import token  # get token

# import discord bot libraries
from discord.ext import commands
# import libraries
import discord
import asyncio
import json


def get_prefix(bot, message):
    """
    Get the prefix for the server the message was sent in
    :param bot: bot object
    :param message: message object
    """
    with open('private/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


# activate intents and set bot prefix with get_prefix function
intents = discord.Intents.default()
intents.presences = True
intents.members = True
bot = commands.Bot(command_prefix=(get_prefix), intents=intents)

# remove help command to use the custom one
bot.remove_command('help')


async def status_task():
    """
    Change bot status
    """
    i = 0
    while True:
        activities = [
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
                name=f'on {len(bot.guilds)} servers'
            ),
            discord.Activity(
                type=discord.ActivityType.watching,
                name=f'on {len(set(bot.get_all_members()))} users'
            ),
            discord.Activity(
                type=discord.ActivityType.playing,
                name='Get bot prefix by mention @FeurBot'
            )
        ]  # list of bot activities
        try:
            await bot.change_presence(activity=activities[i])
            i += 1
            if i > (len(activities) - 1):
                i = 0
            await asyncio.sleep(5)
        except:
            pass


@bot.event
async def on_ready():
    """
    Print in the console when the bot is ready
    Change the bot status
    """
    print(f'{bot.user} is online and connected to {len(bot.guilds)} servers, with {len(set(bot.get_all_members()))} users!')
    bot.loop.create_task(status_task())

"""
# load all the cogs
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
bot.load_extension("cogs.BotInfo")
bot.load_extension("cogs.PlaySound")
bot.load_extension("cogs.CogsManagement")
bot.load_extension("cogs.MemberJoinLeave")
bot.load_extension("cogs.PrefixManagement")
bot.load_extension("cogs.UserManagement")
bot.load_extension("cogs.QuizSystem")
bot.load_extension("cogs.LevelingSystem")
bot.load_extension("cogs.BotChannelManagement")
bot.load_extension("cogs.EconomySystem")
bot.load_extension("cogs.TalkAs")
bot.load_extension("cogs.DeletedMessage")
bot.load_extension("cogs.GifSystem")
"""


# run bot
bot.run(token)
