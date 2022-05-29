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
        music_commands.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        music_commands.set_footer(text="Bot made by @isnubi#6221. If you want to contribute, contact him on discord. If you want to report a bug, contact the developer on discord.")
        
        moderation_commands = discord.Embed(title="**Commands list**", description="List of all the commands available and possible to execute", color=discord.Colour.blue())
        moderation_commands.add_field(name="__Moderation__", value="List of all the moderation commands available", inline=False)
        moderation_commands.add_field(name=f"**{prefix_check(ctx.guild)}purge** *<number>*", value="Delete messages in channel", inline=True)
        moderation_commands.add_field(name=f"**{prefix_check(ctx.guild)}setprefix** *<prefix>*", value="Change the prefix of the bot", inline=True)
        moderation_commands.add_field(name=f"**{prefix_check(ctx.guild)}kick** *<@user>*", value="Kick the mentioned user", inline=True)
        moderation_commands.add_field(name=f"**{prefix_check(ctx.guild)}ban** *<@user>*", value="Ban the mentioned user", inline=True)
        moderation_commands.add_field(name=f"**{prefix_check(ctx.guild)}banlist**", value="List of all the banned users", inline=True)
        moderation_commands.add_field(name=f"**{prefix_check(ctx.guild)}unban** *<userid>*", value="Unban the mentioned user", inline=True)
        moderation_commands.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        moderation_commands.set_footer(text="Bot made by @isnubi#6221. If you want to contribute, contact him on discord. If you want to report a bug, contact the developer on discord.")

        pages = [user_commands, fun_commands, leveling_commands, music_commands, moderation_commands]

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
                if i < 4:
                    i += 1
                    await message.edit(embed=pages[i])

            reaction, user = await self.bot.wait_for('reaction_add', timeout=30, check=check)
            await message.remove_reaction(reaction, user)

        await message.clear_reactions()


def setup(bot):
    """
    Initializes the cog
    :param bot: The bot to initialize the cog with
    """
    bot.add_cog(Help(bot))
    print('Help is loaded')
