import discord
from discord.ext import commands
import json


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
        with open('private/custom_channel.json', 'r') as f:
            custom_channel = json.load(f)
        channel = self.bot.get_channel(int(custom_channel[str(member.guild.id)]["channel"]))
        embed = discord.Embed(
            title=f"Welcome {member.name} to the server!",
            description="Your daily reward of 100 coins have been add yo your balance!",
            color=discord.Color.green()
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.display_avatar.url)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        """
        Sends a message in the system channel when a member leaves a server
        :param member: The member that left the server
        """
        with open('private/custom_channel.json', 'r') as f:
            custom_channel = json.load(f)
        channel = self.bot.get_channel(int(custom_channel[str(member.guild.id)]["channel"]))
        embed = discord.Embed(
            title=f"{member.name} has left the server!",
            description=f"{member.mention} has left the server!",
            color=discord.Color.red()
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.display_avatar.url)
        await channel.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(
        MemberJoinLeave(bot),
        guilds=[discord.Object(id=980975086154682378)])