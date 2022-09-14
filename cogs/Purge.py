import discord
from discord import app_commands
from discord.ext import commands


class Purge(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with
        """
        self.bot = bot

    @app_commands.command(
        name="purge",
        description="Purge messages from a channel")
    @app_commands.describe(
        amount="The amount of messages to purge")
    @commands.has_permissions(administrator=True)
    async def purge(self, interaction: discord.Interaction, amount: int) -> None:
        """
        Purges a specified amount of messages from the channel
        :param interaction: The interaction to respond to.
        :param amount: The amount of messages to purge
        :param amount: The amount of messages to purge
        """
        await interaction.response.defer()
        await interaction.channel.purge(limit=amount)


async def setup(bot: commands.Bot):
    await bot.add_cog(
        Purge(bot),
        guilds=[discord.Object(id=980975086154682378)]
    )
