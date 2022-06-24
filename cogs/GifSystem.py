from discord.ext import commands
import discord
import json
import aiohttp
import random
from private.config import giphy_api_key


class GifSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=bot.loop)

    @commands.command(name='giphy', aliases=['g'], pass_context=True)
    async def giphy(self, ctx, *, search):
        """
        Get a random gif from giphy
        :param ctx: context object
        :param search: search query
        """
        embed = discord.Embed(color=discord.Color.blue())
        if search is None:
            response = await self.session.get('https://api.giphy.com/v1/gifs/random?api_key=' + giphy_api_key)
            data = json.loads(await response.text())
            embed.set_image(url=data['data']['original']['url'])
        else:
            search.replace(' ', '+')
            response = await self.session.get('https://api.giphy.com/v1/gifs/search?&q=api_key=' + search + '&api_key=' + giphy_api_key)
            data = json.loads(await response.text())
            gif_choice = random.randint(0, 9)
            embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

        await self.session.close()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(GifSystem(bot))
    print('GifSystem is loaded')
