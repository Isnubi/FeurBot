from discord.ext import commands
import discord
import json
import asyncio


def prefix_check(guild):
    """
    Checks the guild's prefix
    :param guild: The guild to check
    """
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
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with
        """
        self.bot = bot
    
    @commands.command()
    async def help(self, ctx):
        """
        Sends the help menu in an embed message with pages
        :param ctx: The context of the command
        """
        user_commands = discord.Embed(title="**Commands list**", description="List of all the commands available and possible to execute", color=discord.Colour.blue())
        user_commands.add_field(name='__User__', value='List of all the user commands available', inline=False)
        user_commands.add_field(name=f"**{prefix_check(ctx.guild)}say** *<something>*", value="Let the bot say something you tell it", inline=True)
        user_commands.add_field(name=f"**{prefix_check(ctx.guild)}pfp** *<@user>*", value="Return the profile picture of mentioned user", inline=True)
        user_commands.add_field(name=f"**{prefix_check(ctx.guild)}roll** *<number>**d**<number>*", value="Roll number of dices with the number of sides you tell it\nYou can\'t roll more than 100 dices\nDices can't have more than 100 sides", inline=False)
        user_commands.add_field(name=f"**{prefix_check(ctx.guild)}userinfo** *<@user>* - [ui, user]", value="Get user information", inline=True)
        user_commands.add_field(name=f"**{prefix_check(ctx.guild)}serverinfo** - [si, server]", value="Get server information", inline=True)
        user_commands.add_field(name=f"**{prefix_check(ctx.guild)}botinfo** - [bi, bot]", value="Get bot information", inline=True)
        user_commands.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        user_commands.set_footer(text="Bot made by @isnubi#6221. If you want to contribute, contact him on discord. If you want to report a bug, contact the developer on discord.")

        fun_commands = discord.Embed(title="**Commands list**", description="List of all the commands available and possible to execute", color=discord.Colour.blue())
        fun_commands.add_field(name="__Fun__", value="List of all the fun commands available", inline=False)
        fun_commands.add_field(name=f"**{prefix_check(ctx.guild)}quiz** -[q]", value="Play a quiz", inline=True)
        fun_commands.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        fun_commands.set_footer(text="Bot made by @isnubi#6221. If you want to contribute, contact him on discord. If you want to report a bug, contact the developer on discord.")

        economy_commands = discord.Embed(title="**Commands list**", description="List of all the commands available and possible to execute", color=discord.Colour.blue())
        economy_commands.add_field(name="__Economy__", value="List of all the economy commands available", inline=False)
        economy_commands.add_field(name=f"**{prefix_check(ctx.guild)}register** - [r]", value="Register your account if you don't have any one", inline=True)
        economy_commands.add_field(name=f"**{prefix_check(ctx.guild)}balance** - [b]", value="Get your balance", inline=True)
        economy_commands.add_field(name=f"**{prefix_check(ctx.guild)}daily** - [d]", value="Get your daily reward every 24 hours", inline=True)
        economy_commands.add_field(name=f"**{prefix_check(ctx.guild)}pay** *<@user>* *<amount>*", value="Pay someone money", inline=True)

        leveling_commands = discord.Embed(title="**Commands list**", description="List of all the commands available and possible to execute", color=discord.Colour.blue())
        leveling_commands.add_field(name="__Leveling__", value="List of all the leveling commands available", inline=False)
        leveling_commands.add_field(name=f"**{prefix_check(ctx.guild)}level** *<@user>*", value="Get the level of the mentioned user", inline=True)
        leveling_commands.add_field(name=f"**{prefix_check(ctx.guild)}leaderboard**", value="Get the leaderboard", inline=True)
        leveling_commands.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        leveling_commands.set_footer(text="Bot made by @isnubi#6221. If you want to contribute, contact him on discord. If you want to report a bug, contact the developer on discord.")
        
        music_commands = discord.Embed(title="**Commands list**", description="List of all the commands available and possible to execute", color=discord.Colour.blue())
        music_commands.add_field(name="__Music__", value="List of all the music commands available", inline=False)
        music_commands.add_field(name=f"**{prefix_check(ctx.guild)}join**", value="Join the channel you're in", inline=True)
        music_commands.add_field(name=f"**{prefix_check(ctx.guild)}play** *<url>*", value="Play a song from youtube", inline=True)
        music_commands.add_field(name=f"**{prefix_check(ctx.guild)}pause**", value="Pause the current song", inline=True)
        music_commands.add_field(name=f"**{prefix_check(ctx.guild)}resume**", value="Resume the current song", inline=True)
        music_commands.add_field(name=f"**{prefix_check(ctx.guild)}stop**", value="Stop the music", inline=True)
        music_commands.add_field(name=f"**{prefix_check(ctx.guild)}volume** *<number>*", value="Change the volume of the music", inline=True)
        music_commands.add_field(name=f"**{prefix_check(ctx.guild)}leave**", value="Leave the channel you're in", inline=True)
        music_commands.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        music_commands.set_footer(text="Bot made by @isnubi#6221. If you want to contribute, contact him on discord. If you want to report a bug, contact the developer on discord.")
        
        moderation_commands = discord.Embed(title="**Commands list**", description="List of all the commands available and possible to execute", color=discord.Colour.blue())
        moderation_commands.add_field(name="__Moderation__", value="List of all the moderation commands available\nThese commands are limited for user with privileges in order of the command", inline=False)
        moderation_commands.add_field(name=f"**{prefix_check(ctx.guild)}purge** *<number>*", value="Delete messages in channel", inline=True)
        moderation_commands.add_field(name=f"**{prefix_check(ctx.guild)}setprefix** *<prefix>*", value="Change the prefix of the bot", inline=True)
        moderation_commands.add_field(name=f"**{prefix_check(ctx.guild)}kick** *<@user>*", value="Kick the mentioned user", inline=True)
        moderation_commands.add_field(name=f"**{prefix_check(ctx.guild)}ban** *<@user>*", value="Ban the mentioned user", inline=True)
        moderation_commands.add_field(name=f"**{prefix_check(ctx.guild)}banlist**", value="List of all the banned users", inline=True)
        moderation_commands.add_field(name=f"**{prefix_check(ctx.guild)}unban** *<userid>*", value="Unban the mentioned user", inline=True)
        moderation_commands.add_field(name=f"**{prefix_check(ctx.guild)}mute** *<@user>*", value="Mute the mentioned user", inline=True)
        moderation_commands.add_field(name=f"**{prefix_check(ctx.guild)}unmute** *<@user>*", value="Unmute the mentioned user", inline=True)
        moderation_commands.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        moderation_commands.set_footer(text="Bot made by @isnubi#6221. If you want to contribute, contact him on discord. If you want to report a bug, contact the developer on discord.")

        systemchannel_commands = discord.Embed(title="**Commands list**", description="List of all the commands available and possible to execute", color=discord.Colour.blue())
        systemchannel_commands.add_field(name="__System channel__", value="List of all the system channel commands available\nThese commands are limited for user with **manage channel** permission", inline=False)
        systemchannel_commands.add_field(name=f"**{prefix_check(ctx.guild)}setchannel** *<channel>*", value="Set the channel where the bot will send the messages", inline=True)
        systemchannel_commands.add_field(name=f"**{prefix_check(ctx.guild)}resetchannel**", value="Reset the channel where the bot will send the messages", inline=True)
        systemchannel_commands.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        systemchannel_commands.set_footer(text="Bot made by @isnubi#6221. If you want to contribute, contact him on discord. If you want to report a bug, contact the developer on discord.")

        prefix_commands = discord.Embed(title="**Commands list**", description="List of all the commands available and possible to execute", color=discord.Colour.blue())
        prefix_commands.add_field(name="__Prefix__", value="List of all the prefix commands available\nThese commands are limited for user with **administrator** privileges", inline=False)
        prefix_commands.add_field(name=f"**Mention the bot**", value="Mention the bot to get the prefix", inline=True)
        prefix_commands.add_field(name=f"**{prefix_check(ctx.guild)}setprefix** *<prefix>*", value="Change the prefix of the bot", inline=True)
        prefix_commands.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        prefix_commands.set_footer(text="Bot made by @isnubi#6221. If you want to contribute, contact him on discord. If you want to report a bug, contact the developer on discord.")

        hardware_commands = discord.Embed(title="**Commands list**", description="List of all the commands available and possible to execute", color=discord.Colour.blue())
        hardware_commands.add_field(name="__Hardware__", value="List of all the hardware commands available", inline=False)
        hardware_commands.add_field(name=f"**{prefix_check(ctx.guild)}ping**", value="Get the latency of the bot", inline=True)
        hardware_commands.add_field(name=f"**{prefix_check(ctx.guild)}cpu**", value="Get the CPU usage of the bot", inline=True)
        hardware_commands.add_field(name=f"**{prefix_check(ctx.guild)}ram**", value="Get the RAM usage of the bot", inline=True)
        hardware_commands.add_field(name=f"**{prefix_check(ctx.guild)}temp**", value="Get the temperature of the bot", inline=True)
        hardware_commands.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        hardware_commands.set_footer(text="Bot made by @isnubi#6221. If you want to contribute, contact him on discord. If you want to report a bug, contact the developer on discord.")

        pages = [user_commands, fun_commands, economy_commands, leveling_commands, music_commands, moderation_commands, systemchannel_commands, prefix_commands, hardware_commands]

        await ctx.message.delete()
        message = await ctx.send(embed=pages[0])
        await message.add_reaction('◀')
        await message.add_reaction('▶')

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ['◀', '▶']

        i = 0
        reaction = None
        while True:
            if str(reaction) == '◀':
                if i > 0:
                    i -= 1
                    await message.edit(embed=pages[i])
            elif str(reaction) == '▶':
                if i < len(pages) - 1:
                    i += 1
                    await message.edit(embed=pages[i])

            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                await message.delete()
                return
            else:
                await message.remove_reaction(reaction, user)

        await message.clear_reactions()


def setup(bot):
    """
    Initializes the cog
    :param bot: The bot to initialize the cog with
    """
    bot.add_cog(Help(bot))
    print('Help is loaded')
