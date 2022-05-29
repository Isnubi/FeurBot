from discord.ext import commands


class Purge(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with
        """
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.command(name="purge")
    async def purge(self, ctx, purge_amount: int):
        """
        Purges a specified amount of messages from the channel
        :param ctx: The context of the command
        :param purge_amount: The amount of messages to purge
        """
        await ctx.channel.purge(limit=purge_amount)


def setup(bot):
    """
    Initializes the cog
    :param bot: bot object
    """
    bot.add_cog(Purge(bot))
    print('Purge is loaded')
