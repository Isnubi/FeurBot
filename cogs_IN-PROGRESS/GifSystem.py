from discord.ext import commands
import discord
import json
import aiohttp
import random
from private.config import giphy_api_key


class GifSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='giphy', aliases=['g'], pass_context=True)
    async def giphy(self, ctx, *, search=None):
        """
        Get a random gif from giphy
        :param ctx: context object
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
        await ctx.message.delete()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(GifSystem(bot))
    print('GifSystem is loaded')
