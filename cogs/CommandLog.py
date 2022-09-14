import discord
from discord import app_commands
from discord.ext import commands


class CommandLog(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with.
        """
        self.bot = bot

    # check if app command is used
    @commands.Cog.listener(name='on_interaction')
    async def on_interaction(self, interaction: discord.Interaction):
        """
        Check if app command is used
        :param interaction: The interaction to check
        """
        print(f'{interaction.command.name} executed by {interaction.user} on the server {interaction.guild} || at '
              f'{interaction.created_at} UTC')

    @commands.Cog.listener(name='on_command')
    async def on_command(self, ctx):
        """
        Logs the command sent by the user
        :param ctx: The context of the command
        """
        print(f'{ctx.command} executed by {ctx.author} on the server {ctx.guild.name} || at '
              f'{ctx.message.created_at} UTC')


async def setup(bot: commands.Bot):
    await bot.add_cog(
        CommandLog(bot),
        guilds=[discord.Object(id=980975086154682378)])
