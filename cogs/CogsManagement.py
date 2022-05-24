from discord.ext import commands
import discord


class CogsManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            embed = discord.Embed(title='**An error has occured:**', description=f'{type(e).__name__} - {e}', color=0xff0000)
        else:
            embed = discord.Embed(title='**Successfully loaded:**', description=cog, color=0x008000)

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            embed = discord.Embed(title='**An error has occured:**', description=f'{type(e).__name__} - {e}', color=0xff0000)
        else:
            embed = discord.Embed(title='**Successfully unloaded:**', description=cog, color=0x008000)

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            embed = discord.Embed(title='**An error has occured:**', description=f'{type(e).__name__} - {e}', color=0xff0000)
        else:
            embed = discord.Embed(title='**Successfully reloaded:**', description=cog, color=0x008000)

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        await ctx.message.delete()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(CogsManagement(bot))
    print('CogsManagement is loaded')
