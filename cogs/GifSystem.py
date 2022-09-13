import discord
from discord import app_commands
from discord.ext import commands
import json
import aiohttp
import random
from private.config import giphy_api_key


class GifSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="gif",
        description="Get a random gif from Giphy")
    @app_commands.describe(
        search="The search term to query Giphy for")
    async def gif(self, interaction: discord.Interaction, *, search: str = None) -> None:
        """
        Get a random gif from giphy
        :param search: search query
        """
        session = aiohttp.ClientSession()
        embed = discord.Embed(color=discord.Color.blue())
        if not search:
            eq_response = await session.get('https://api.giphy.com/v1/gifs/random?api_key=' + giphy_api_key)
            data = json.loads(await eq_response.text())
            embed.set_image(url=data['data']['images']['original']['url'])
        else:
            search.replace(' ', '+')
            q_response = await session.get('https://api.giphy.com/v1/gifs/search?&q=api_key=' + search + '&api_key=' + giphy_api_key)
            data = json.loads(await q_response.text())
            gif_choice = random.randint(0, 9)
            embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

        await session.close()
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(
        GifSystem(bot),
        guilds=[discord.Object(id=980975086154682378)]
    )
