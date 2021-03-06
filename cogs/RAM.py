from discord.ext import commands
import discord
import psutil


class RAM(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with
        """
        self.bot = bot

    @commands.command(name='ram')
    async def ram(self, ctx):
        """
        Displays the current RAM usage of the server where the bot is running
        :param ctx: The context of the command
        """
        ram_usage = psutil.virtual_memory().percent
        ram_message = 'Memory is used at ' + str(ram_usage) + '%'
        embed = discord.Embed(title="Memory usage", description=ram_message, color=discord.Colour.blue())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

        await ctx.message.delete()
        await ctx.send(embed=embed)


def setup(bot):
    """
    Initializes the cog
    :param bot: bot object
    """
    bot.add_cog(RAM(bot))
    print('RAM is loaded')
