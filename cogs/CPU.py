from discord.ext import commands
import discord
import psutil


class CPU(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with.
        """
        self.bot = bot

    @commands.command(name='cpu')
    async def cpu(self, ctx):
        """
        Displays the CPU usage of the server where the bot is running
        :param ctx: The context of the command
        """
        cpu_usage = psutil.cpu_percent(interval=0.5)
        cpu_message = 'CPU is used at ' + str(cpu_usage) + '%'
        embed = discord.Embed(title="CPU usage", description=cpu_message, color=discord.Colour.blue())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

        await ctx.message.delete()
        await ctx.send(embed=embed)


def setup(bot):
    """
    Initializes the cog
    :param bot: bot object
    """
    bot.add_cog(CPU(bot))
    print('CPU is loaded')

