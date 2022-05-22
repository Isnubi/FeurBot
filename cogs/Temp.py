from discord.ext import commands
import subprocess
import discord


class Temp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # command to show Raspberry Pi temperature
    @commands.command()
    async def temp(self, ctx):
        temp_result = subprocess.run(['cat', '/home/isnubi/discordpy/temp'], stdout=subprocess.PIPE) # replace path to /sys/class/thermal/thermal_zone0/temp if you have sudo rights on the host
        temp_result = temp_result.stdout.decode('utf-8')
        temp_message = temp_result[0:2] + '.' + temp_result[3] + '°C'
        if int(temp_result[0:2]) < 45:
            temp_embed = discord.Embed(title="Température", description=temp_message, color=0x008000)
        elif int(temp_result[0:2]) >= 50:
            temp_embed = discord.Embed(title="Température", description=temp_message, color=0xff0000)
        else:
            temp_embed = discord.Embed(title="Température", description=temp_message, color=0xff7f00)
        await ctx.send(embed=temp_embed)


def setup(bot):
    bot.add_cog(Temp(bot))
