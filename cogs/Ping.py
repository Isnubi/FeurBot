from discord.ext import commands
import discord


class Ping(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with
        """
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx):
        """
        Command to check the latency of the bot
        :param ctx: The context of the command
        """
        embed = discord.Embed(title="Pong!", description='Bot have {0}ms of delay'.format(round(self.bot.latency * 1000)), color=discord.Colour.blue())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    """
    Initializes the cog
    :param bot: bot object
    """
    bot.add_cog(Ping(bot))
    print('Ping is loaded')
