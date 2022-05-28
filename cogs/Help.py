from discord.ext import commands
import discord
import json


def prefix_check(guild):
    if guild is None:
        return '!'
    try:
        with open('private/prefixes.json', 'r') as f:
            prefixes = json.load(f)
            return prefixes[str(guild.id)]
    except:
        return '!'


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):
        embed = discord.Embed(title="**Commands list**", description="List of all the commands available and possible to execute", color=discord.Colour.blue())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

        # Hardware command
        embed.add_field(name="__Hardware__", value="List of all the hardware commands available", inline=False)
        embed.add_field(name=f'**{prefix_check(ctx.guild)}cpu**', value="Check the CPU usage", inline=True)
        embed.add_field(name=f'**{prefix_check(ctx.guild)}ram**', value="Check the memory usage", inline=True)
        embed.add_field(name=f"**{prefix_check(ctx.guild)}temp**", value="Check the temp", inline=True)
        embed.add_field(name=f"**{prefix_check(ctx.guild)}ping**", value="Check the bot latency", inline=True)

        # User command
        embed.add_field(name="__User__", value="List of all the user commands available", inline=False)
        embed.add_field(name=f"**{prefix_check(ctx.guild)}say** *<something>*", value="Let the bot say something you tell it", inline=True)
        embed.add_field(name=f"**{prefix_check(ctx.guild)}pfp** *<@user>*", value="Return the profile picture of mentioned user", inline=True)
        embed.add_field(name=f"**{prefix_check(ctx.guild)}roll** *<number>**d**<number>*", value="Roll number of dices with the number of sides you tell it\nYou can\'t roll more than 100 dices\nDices can't have more than 100 sides", inline=False)
        embed.add_field(name=f"**{prefix_check(ctx.guild)}userinfo** *<@user>* - [ui, user]", value="Get user information", inline=True)
        embed.add_field(name=f"**{prefix_check(ctx.guild)}serverinfo** - [si, server]", value="Get server information", inline=True)
        embed.add_field(name=f"**{prefix_check(ctx.guild)}quiz** -[q]", value="Play a quiz", inline=True)

        # Music command
        embed.add_field(name="__Music__", value="List of all the music commands available", inline=False)
        embed.add_field(name=f"**{prefix_check(ctx.guild)}join**", value="Join the channel you're in", inline=True)
        embed.add_field(name=f"**{prefix_check(ctx.guild)}play** *<url>*", value="Play a song from youtube", inline=True)
        embed.add_field(name=f"**{prefix_check(ctx.guild)}pause**", value="Pause the current song", inline=True)
        embed.add_field(name=f"**{prefix_check(ctx.guild)}resume**", value="Resume the current song", inline=True)
        embed.add_field(name=f"**{prefix_check(ctx.guild)}stop**", value="Stop the music", inline=True)
        embed.add_field(name=f"**{prefix_check(ctx.guild)}volume** *<number>*", value="Change the volume of the music", inline=True)

        # Admin command
        for role in ctx.message.author.roles:
            if role.name == 'Bot':  # replace with your admin privileges role name
                embed.add_field(name="__Admin__", value="List of all the admin commands available", inline=False)
                embed.add_field(name=f"**{prefix_check(ctx.guild)}purge** *<number>*", value="Delete messages in channel", inline=True)
                embed.add_field(name=f"**{prefix_check(ctx.guild)}setprefix** *<prefix>*", value="Change the prefix of the bot", inline=True)
                embed.add_field(name=f"**{prefix_check(ctx.guild)}kick** *<@user>*", value="Kick the mentioned user", inline=True)
                embed.add_field(name=f"**{prefix_check(ctx.guild)}ban** *<@user>*", value="Ban the mentioned user", inline=True)
                embed.add_field(name=f"**{prefix_check(ctx.guild)}banlist**", value="List of all the banned users", inline=True)
                embed.add_field(name=f"**{prefix_check(ctx.guild)}unban** *<userid>*", value="Unban the mentioned user", inline=True)

        embed.set_footer(text="Bot made by @isnubi#6221. If you want to contribute, contact him on discord. If you want to report a bug, contact the developer on discord.")

        await ctx.message.delete()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
    print('Help is loaded')
