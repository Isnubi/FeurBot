import discord
from discord import app_commands
from discord.ext import commands
import psutil


class RAM(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with
        """
        self.bot = bot

    @app_commands.command(
        name="ram",
        description="Get the current RAM usage of the bot")
    async def ram(self, interaction: discord.Interaction) -> None:
        """
        Displays the current RAM usage of the server where the bot is running
        """
        ram_usage = psutil.virtual_memory().percent
        ram_message = 'Memory is used at ' + str(ram_usage) + '%'
        await interaction.response.send_message(ram_message)


async def setup(bot: commands.Bot):
    await bot.add_cog(
        RAM(bot),
        guilds=[discord.Object(id=980975086154682378)]
    )
