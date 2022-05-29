from discord.ext import commands
import discord


class MemberJoinLeave(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """
        Sends a message in the system channel when a member joins a server
        :param member: The member that joined the server
        """
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
        """
        Sends a message in the system channel when a member leaves a server
        :param member: The member that left the server
        """
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
    """
    Initializes the cog
    :param bot: bot object
    """
    bot.add_cog(MemberJoinLeave(bot))
    print('Test is loaded')
