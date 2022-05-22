from discord.ext import commands
import discord


class PP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pp(self, ctx):
        user = ctx.message.author
        pfp = user.avatar_url
        embed = discord.Embed(title='Here\'s {0} avatar'.format(user.name), color=0xecce8b)
        embed.set_image(url=pfp)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(PP(bot))
