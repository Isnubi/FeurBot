import discord
from discord import app_commands
from discord.ext import commands


class ProfilePicture(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with
        """
        self.bot = bot

    @app_commands.command(
        name="profilepicture",
        description="Get the current delay of the bot")
    async def profilepicture(self, interaction: discord.Interaction, person: discord.User) -> None:
        """
        Command to get the profile picture of a user
        :param person: The user to get the profile picture of
        """
        user = person
        pfp = user.display_avatar.url
        embed = discord.Embed(title='Here\'s {0.name} avatar'.format(user), color=discord.Colour.blue())
        embed.set_image(url=pfp)
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(
        ProfilePicture(bot),
        guilds=[discord.Object(id=980975086154682378)]
    )
