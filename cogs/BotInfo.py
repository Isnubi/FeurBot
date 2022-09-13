import discord
from discord import app_commands
from discord.ext import commands
import json


class BotInfo(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with.
        """
        self.bot = bot


    @app_commands.command(
        name="botinfo",
        description="Get the bot info")
    async def botinfo(self, interaction: discord.Interaction) -> None:
        """
        Get the bot info.
        """

        embed = discord.Embed(title=self.bot.user.name, description='Information of this bot',
                              color=discord.Colour.blue())
        embed.set_thumbnail(url=self.bot.user.display_avatar.url)
        embed.set_footer(text=f'This bot is running on {len(self.bot.guilds)} servers!')
        embed.add_field(name='Bot Name', value=self.bot.user.name, inline=True)
        embed.add_field(name='Bot Version', value='1.3.7', inline=True)
        #embed.add_field(name='Bot Prefix', value=f"{prefix_check(ctx.guild)}", inline=True)
        embed.add_field(name='Bot Language', value='Python 3.7', inline=True)
        embed.add_field(name='Bot Library', value='discord.py', inline=True)
        embed.add_field(name='Bot Developer: isnubi#6221', value='https://github.com/Isnubi/', inline=False)
        embed.add_field(name='Bot GitHub', value='https://github.com/Isnubi/FeurBot', inline=False)

        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(
        BotInfo(bot),
        guilds=[discord.Object(id=980975086154682378)]
    )
