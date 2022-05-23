from discord.ext import commands
import discord


class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='userinfo', aliases=['user', 'ui'])
    async def userinfo(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        date_format = '%Y-%m-%d %H:%M:%S'
        embed = discord.Embed(title=f'{member}', description='Information of this user', color=discord.Colour.blue())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name='Joined Server', value=member.joined_at.strftime(date_format), inline=True)
        embed.add_field(name='Account Created', value=member.created_at.strftime(date_format), inline=True)
        if member.status is not None:
            if member.status == discord.Status.online:
                embed.add_field(name='Status', value='Online', inline=True)
            elif member.status == discord.Status.idle:
                embed.add_field(name='Status', value='Idle', inline=True)
            elif member.status == discord.Status.dnd:
                embed.add_field(name='Status', value='Do Not Disturb', inline=True)
            elif member.status == discord.Status.offline:
                embed.add_field(name='Status', value='Offline', inline=True)
        embed.add_field(name='Bot', value=member.bot, inline=True)
        if str(member.colour) != '#000000':
            embed.add_field(name='Color', value=member.colour, inline=True)
        if member.nick is not None:
            embed.add_field(name='Nickname', value=member.nick, inline=True)
        embed.add_field(name='Roles', value=', '.join([role.mention for role in member.roles]), inline=True)
        if member.premium_since is not None:
            embed.add_field(name='Boosting Since', value=member.premium_since.strftime(date_format), inline=True)
        embed.set_footer(text=f'User ID: {member.id}')

        await ctx.message.delete()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(UserInfo(bot))
    print('UserInfo is loaded')
