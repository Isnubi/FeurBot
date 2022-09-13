from discord.ext import commands
import discord


class CogsManagement(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with.
        """
        self.bot = bot

    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        """
        Loads a cog.
        :param ctx: The context of the command
        :param cog: The name of the cog to load
        """
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
        """
        Unloads a cog.
        :param ctx: The context of the command
        :param cog: The name of the cog to unload
        """
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
        """
        Reloads a cog.
        :param ctx: The context of the command
        :param cog: The name of the cog to reload
        """
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

    @commands.is_owner()
    @commands.command(name='reloadall', hidden=True)
    async def reloadall(self, ctx):
        """
        Reloads all cogs
        :param ctx: The context of the command
        """
        for cog in self.bot.cogs:
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

    @commands.command(name='coglist', hidden=True)
    @commands.is_owner()
    async def coglist(self, ctx):
        """
        Lists all cogs
        :param ctx: The context of the command
        """
        embed = discord.Embed(title='**Cogs:**', description='\n'.join([f'{cog}' for cog in self.bot.cogs]), color=discord.Color.blue())
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        await ctx.message.delete()
        await ctx.send(embed=embed)


def setup(bot):
    """
    Initializes the cog
    :param bot: bot object
    """
    bot.add_cog(CogsManagement(bot))
    print('CogsManagement is loaded')
