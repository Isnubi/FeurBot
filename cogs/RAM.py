from discord.ext import commands
import discord
import psutil


class RAM(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # command to get global memory usage via psutil
    @commands.command()
    async def ram(self, ctx):
        ram_usage = psutil.virtual_memory().percent
        ram_message = str(ram_usage) + '%'
        embed_ram = discord.Embed(title="Usage de la RAM", description=ram_message, color=0x008000)
        await ctx.send(embed=embed_ram)  # command to get global memory usage via psutil


def setup(bot):
    bot.add_cog(RAM(bot))
