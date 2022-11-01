# get token
from private.config import token

# import discord bot libraries
import discord
from discord import app_commands
from discord.ext import commands
# import libraries
import asyncio
import datetime
# import mysql connector and database credentials
import mysql.connector
from private.config import mysql_host, mysql_user, mysql_password, mysql_database

mydb = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database)

mycursor = mydb.cursor(buffered=True)


class FeurBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='!',
            description='FeurBot is a bot made by isnubi#6221',
            intents=discord.Intents.All(),
            application_id=1019244895589892167,
            help_command=None
        )

        self.initial_extensions = [
            'cogs.Ping',
            'cogs.QuoiFeur',
            'cogs.BotInfo',
            'cogs.UserInfo',
            'cogs.CPU',
            'cogs.RAM',
            'cogs.ProfilePicture',
            'cogs.GifSystem',
            'cogs.Roll',
            'cogs.ServerInfo',
            'cogs.CommandLog',
            'cogs.Purge',
            'cogs.Help',
            'cogs.DeletedMessage',
            'cogs.BotChannelManagement',
            'cogs.MemberJoinLeave',
            'cogs.UserManagement',
            'cogs.GuildJoinLeave',
            'cogs.LevelingSystem',
            'cogs.EconomySystem'
        ]

    async def setup_hook(self):
        for extension in self.initial_extensions:
            await self.load_extension(extension)

        await bot.tree.sync(guild=discord.Object(id=980975086154682378))

    async def on_ready(self):
        """
            Print in the console when the bot is ready
            Change the bot status
        """
        print(f'{self.user} is online and connected to {len(self.guilds)} servers, with {len(set(self.get_all_members()))} users!')
        self.loop.create_task(status_task())


bot = FeurBot()


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


bot.run(token)
