from discord.ext import commands
import subprocess
import discord


class Temp(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with
        """
        self.bot = bot

    @commands.command(name='temp')
    async def temp(self, ctx):
        """
        Gets the current temperature of the server where the bot is running
        :param ctx: The context of the command
        """
        temp_result = subprocess.run(['cat', '/home/isnubi/discordpy/temp'], stdout=subprocess.PIPE) # replace path to /sys/class/thermal/thermal_zone0/temp if you have sudo rights on the host
        temp_result = temp_result.stdout.decode('utf-8')
        temp_message = 'CPU temperature is ' + temp_result[0:2] + '.' + temp_result[3] + '°C'
        if int(temp_result[0:2]) < 45:
            embed = discord.Embed(title="Temperature", description=temp_message, color=0x008000)
        elif int(temp_result[0:2]) >= 50:
            embed = discord.Embed(title="Temperature", description=temp_message, color=0xff0000)
        else:
            embed = discord.Embed(title="Temperature", description=temp_message, color=0xff7f00)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

        await ctx.message.delete()
        await ctx.send(embed=embed)


def setup(bot):
    """
    Initializes the cog
    :param bot: bot object
    """
    bot.add_cog(Temp(bot))
    print('Temp is loaded')
