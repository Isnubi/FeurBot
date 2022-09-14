import discord
from discord import app_commands
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with
        """
        self.bot = bot

    @app_commands.command(
        name="ping",
        description="Get the current delay of the bot")
    async def ping(self, interaction: discord.Interaction) -> None:
        """
        Get the current delay of the bot.
        :param interaction: The interaction to respond to.
        """
        await interaction.response.send_message(f"Pong! {round(self.bot.latency * 1000)}ms")


async def setup(bot: commands.Bot):
    await bot.add_cog(
        Ping(bot),
        guilds=[discord.Object(id=980975086154682378)]
    )
