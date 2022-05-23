from private.config import token  # get token

# import discord bot libraries
from discord.ext import commands


# set box prefix to "!"
bot = commands.Bot(command_prefix='!')
bot.remove_command('help')


# alert in the console when bot is ready
@bot.event
async def on_ready():
    print('Bot ready!')


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

bot.run(token)
