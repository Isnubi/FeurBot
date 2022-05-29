import discord
from discord.ext import commands


class BotInfo(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with.
        """
        self.bot = bot

    @commands.command(name='botinfo', aliases=['bot', 'about', 'bi'])
    async def botinfo(self, ctx):
        """
        Displays information about the bot
        :param ctx: The context of where the command was used
        """
        embed = discord.Embed(title=self.bot.user.name, description='Information of this bot', color=discord.Colour.blue())
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_footer(text=f'This bot is running on {len(self.bot.guilds)} servers!')
        embed.add_field(name='Bot Name', value=self.bot.user.name, inline=True)
        embed.add_field(name='Bot Version', value='1.3.7', inline=True)
        embed.add_field(name='Bot Prefix', value='!', inline=True)
        embed.add_field(name='Bot Language', value='Python 3.7', inline=True)
        embed.add_field(name='Bot Library', value='discord.py', inline=True)
        embed.add_field(name='Bot Developer: isnubi#6221', value='https://github.com/Isnubi/', inline=False)
        embed.add_field(name='Bot GitHub', value='https://github.com/Isnubi/FeurBot', inline=False)

        await ctx.message.delete()
        await ctx.send(embed=embed)


def setup(bot):
    """
    Initializes the cog
    :param bot: bot object
    """
    bot.add_cog(BotInfo(bot))
    print('BotInfo is loaded')
