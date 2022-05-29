from discord.ext import commands
import discord
import json


def prefix_check(guild):
    """
    Checks if the guild has a custom prefix set.
    :param guild: The guild to check.
    """
    if guild is None:
        return '!'
    try:
        with open('private/prefixes.json', 'r') as f:
            prefixes = json.load(f)
            return prefixes[str(guild.id)]
    except:
        return '!'


class PrefixManagement(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """
        Adds the guild to the prefixes.json file
        :param guild: The guild to add
        """
        with open('private/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(guild.id)] = '!'

        with open('private/prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        """
        Removes the guild from the prefixes.json file
        :param guild: The guild to remove
        """
        with open('private/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes.pop(str(guild.id))

        with open('private/prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

    @commands.command(name='changeprefix', aliases=['prefix'])
    @commands.has_permissions(administrator=True)
    async def changeprefix(self, ctx, prefix):
        """
        Changes the prefix for the guild
        :param ctx: The context of the command
        :param prefix: The new prefix
        """
        with open('private/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('private/prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        embed = discord.Embed(title='Changing Prefix', description=f'Prefix changed to:   **{prefix}**', color=discord.Color.blue())
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        """
        Check if the bot is mentioned in the message
        Send the prefix if it is
        :param message: The message to check
        """
        if message.guild.me.mention in message.content:
            embed = discord.Embed(title='Prefix', description=f'My prefix is:   **{prefix_check(message.guild)}**', color=discord.Color.blue())
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f'Requested by {message.author}', icon_url=message.author.avatar_url)

            await message.delete()
            await message.channel.send(embed=embed)


def setup(bot):
    """
    Initializes the cog
    :param bot: bot object
    """
    bot.add_cog(PrefixManagement(bot))
    print('PrefixManagement is loaded')
