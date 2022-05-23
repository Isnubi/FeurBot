from discord.ext import commands
import discord


class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='serverinfo', aliases=['si, server'])
    async def serverinfo(self, ctx):
        embed = discord.Embed(title=f"{ctx.guild.name} Info", description="Information of this server", color=discord.Colour.blue())
        embed.add_field(name='Owner', value=f"{ctx.guild.owner}", inline=True)
        embed.add_field(name='Verification level', value=f"{ctx.guild.verification_level}", inline=True)
        embed.add_field(name='Created On', value=ctx.guild.created_at.strftime("%b %d %Y"), inline=True)
        embed.add_field(name='Total of roles', value=f"{len(ctx.guild.roles)}", inline=True)

        total_bots, total_online = 0, 0
        for member in ctx.guild.members:
            if member.bot:
                total_bots += 1
            if member.status != discord.Status.offline:
                total_online += 1
        embed.add_field(name='Members', value=f"{len(ctx.guild.members)} members,\n{total_online} online,\n{total_bots} bots, {len(ctx.guild.members) - total_bots} humans", inline=True)

        text_channels = ctx.guild.text_channels
        voice_channels = ctx.guild.voice_channels
        categories = ctx.guild.categories
        total_channels = len(text_channels) + len(voice_channels)
        embed.add_field(name='Total of channels', value=f"{total_channels} channels in total:\n{len(categories)} categories\n{len(text_channels)} text, {len(voice_channels)} voice", inline=True)

        embed.add_field(name='Boost level', value=f"{ctx.guild.premium_tier}", inline=True)
        embed.add_field(name='Boosts number', value=f"{ctx.guild.premium_subscription_count}", inline=True)

        embed.set_footer(text=f'Server name: {ctx.guild.name} | Server ID: {ctx.guild.id}')
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_author(name=f'{ctx.author.name}', icon_url=ctx.author.avatar_url)

        await ctx.message.delete()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ServerInfo(bot))
    print('ServerInfo is loaded')
