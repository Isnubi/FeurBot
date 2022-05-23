from discord.ext import commands
import discord


class PP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='pfp')
    async def pfp(self, ctx, person: discord.User):
        user = person
        pfp = user.avatar_url
        embed = discord.Embed(title='Here\'s {0.name} avatar'.format(user), color=discord.Colour.blue())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_image(url=pfp)

        await ctx.message.delete()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(PP(bot))
    print('PFP is loaded')
