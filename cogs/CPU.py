from discord.ext import commands
import discord
import psutil


class CPU(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='cpu')
    async def cpu(self, ctx):
        cpu_usage = psutil.cpu_percent(interval=0.5)
        cpu_message = 'CPU is used at ' + str(cpu_usage) + '%'
        embed = discord.Embed(title="CPU usage", description=cpu_message, color=discord.Colour.blue())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

        await ctx.message.delete()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(CPU(bot))
    print('CPU is loaded')

