from discord.ext import commands
import discord


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx):
        embed = discord.Embed(title="Pong!", description='Bot have {0}ms of delay'.format(round(self.bot.latency * 1000)), color=discord.Colour.blue())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Ping(bot))
