import discord
from discord import app_commands
from discord.ext import commands
import psutil


class CPU(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with.
        """
        self.bot = bot

    @app_commands.command(
        name="cpu",
        description="Get the current CPU usage of the bot")
    async def cpu(self, interaction: discord.Interaction) -> None:
        """
        Displays the CPU usage of the server where the bot is running
        :param interaction: The interaction to respond to.
        """
        cpu_usage = psutil.cpu_percent(interval=0.5)
        cpu_message = 'CPU is used at ' + str(cpu_usage) + '%'
        await interaction.response.send_message(cpu_message)


async def setup(bot: commands.Bot):
    await bot.add_cog(
        CPU(bot),
        guilds=[discord.Object(id=980975086154682378)]
    )
