from discord.ext import commands
import discord


class PP(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with
        """
        self.bot = bot

    @commands.command(name='pfp')
    async def pfp(self, ctx, person: discord.User):
        """
        Command to get the profile picture of a user
        :param ctx: The context of the command
        :param person: The user to get the profile picture of
        """
        user = person
        pfp = user.avatar_url
        embed = discord.Embed(title='Here\'s {0.name} avatar'.format(user), color=discord.Colour.blue())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_image(url=pfp)

        await ctx.message.delete()
        await ctx.send(embed=embed)


def setup(bot):
    """
    Initializes the cog
    :param bot: bot object
    """
    bot.add_cog(PP(bot))
    print('PFP is loaded')
