import discord
from discord import app_commands
from discord.ext import commands


class test(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="introduce",
        description="Introduce yourself to the bot"
    )

    @app_commands.describe(
        name="Your name",
        age="Your age"
    )

    async def introduce(
            self,
            interaction: discord.Interaction,
            name: str,
            age: int):
        await interaction.response.send_message(f"My name is {name} and I am {age} years old")


async def setup(bot: commands.Bot):
    await bot.add_cog(
        test(bot),
        guilds=[discord.Object(id=980975086154682378)]
    )