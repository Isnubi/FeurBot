from discord.ext import commands


class Purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.command(name="purge")
    async def purge(self, ctx, purge_amount: int):
        await ctx.channel.purge(limit=purge_amount)


def setup(bot):
    bot.add_cog(Purge(bot))
    print('Purge is loaded')
