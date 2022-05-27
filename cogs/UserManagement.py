from discord.ext import commands
import discord


class UserManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        embed = discord.Embed(title="Kicked", description=f"{member.mention} has been kicked.", color=0x00ff00)
        embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_author(name=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url)
        await member.kick(reason=reason)
        await ctx.send(embed=embed)

    @commands.command(name='ban')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        embed = discord.Embed(title="Banned", description=f"{member.mention} has been banned.", color=0x00ff00)
        embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_author(name=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url)
        await member.ban(reason=reason)
        await ctx.send(embed=embed)

    @commands.command(name='banlist')
    @commands.has_permissions(ban_members=True)
    async def banlist(self, ctx):
        embed = discord.Embed(title="List of banned users", description="List of banned users.", color=0x00ff00)
        banned = await ctx.guild.bans()
        for user in banned:
            embed.add_field(name=f"{user.user.name}: {user.user.id}", value=f"Banned for {user.reason}", inline=False)
        embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_author(name=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url)
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command(name='unban')
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, id):
        banned_users = await ctx.guild.bans()
        for user in banned_users:
            if str(user.user.id) == id:
                await ctx.guild.unban(user.user)
                embed = discord.Embed(title="Unbanned", description=f"{user.user.mention} has been unbanned.", color=0x00ff00)
                embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
                embed.set_author(name=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url)
                await ctx.message.delete()
                await ctx.send(embed=embed)
                return
            else:
                embed = discord.Embed(title="An error occurred", description="User not found.", color=0xff0000)
                embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
                embed.set_author(name=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url)
                await ctx.message.delete()
                await ctx.send(embed=embed)
                return


def setup(bot):
    bot.add_cog(UserManagement(bot))
    print('UserManagement is loaded')
