from discord.ext import commands


class Purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # command to purge channel with int arg in entry
    @commands.has_permissions(administrator=True)
    @commands.command()
    async def purge(self, ctx, purge_amount: int):
        await ctx.channel.purge(limit=purge_amount)


def setup(bot):
    bot.add_cog(Purge(bot))
