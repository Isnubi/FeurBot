from discord.ext import commands
import discord
import psutil


class CPU(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # command to get global CPU usage via psutil
    @commands.command()
    async def cpu(self, ctx):
        cpu_usage = psutil.cpu_percent(interval=0.5)
        cpu_message = str(cpu_usage) + '%'
        embed_cpu = discord.Embed(title="Usage du CPU", description=cpu_message, color=0x008000)
        await ctx.send(embed=embed_cpu)


def setup(bot):
    bot.add_cog(CPU(bot))
