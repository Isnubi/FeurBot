from private.config import token  # get token

# import discord bot libraries
from discord.ext import commands
import discord

# activate intents and set bot prefix to "!"
intents = discord.Intents.default()
intents.presences = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

# remove help command to use the custom one
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
bot.load_extension("cogs.UserInfo")

bot.run(token)
