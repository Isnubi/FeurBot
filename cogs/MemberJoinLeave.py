from discord.ext import commands
import discord


class MemberJoinLeave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(member.guild.system_channel.id)
        embed = discord.Embed(
            title=f"Welcome {member.name} to the server!",
            description=f"{member.mention} has joined the server!",
            color=discord.Color.green()
        )
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(member.guild.system_channel.id)
        embed = discord.Embed(
            title=f"{member.name} has left the server!",
            description=f"{member.mention} has left the server!",
            color=discord.Color.red()
        )
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(MemberJoinLeave(bot))
    print('Test is loaded')
