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
        embed = discord.Embed(title=f'{member}', description=f'{member.id}', color=discord.Colour.blue())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name='Joined Server', value=member.joined_at.strftime(date_format))
        embed.add_field(name='Account Created', value=member.created_at.strftime(date_format))
        if member.status is not None:
            if member.status == discord.Status.online:
                embed.add_field(name='Status', value='Online')
            elif member.status == discord.Status.idle:
                embed.add_field(name='Status', value='Idle')
            elif member.status == discord.Status.dnd:
                embed.add_field(name='Status', value='Do Not Disturb')
            elif member.status == discord.Status.offline:
                embed.add_field(name='Status', value='Offline')
        embed.add_field(name='Bot', value=member.bot)
        embed.add_field(name='Color', value=member.colour)
        embed.add_field(name='Nickname', value=member.nick)
        embed.add_field(name='Roles', value=', '.join([role.mention for role in member.roles]))
        embed.add_field(name='Top Role', value=member.top_role)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(UserInfo(bot))
    print('UserInfo is loaded')
