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


class PrefixManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open('private/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(guild.id)] = '!'

        with open('private/prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open('private/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes.pop(str(guild.id))

        with open('private/prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

    @commands.command(name='changeprefix', aliases=['prefix'])
    @commands.has_permissions(administrator=True)
    async def changeprefix(self, ctx, prefix):
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
        if self.bot.user.mentioned_in(message):
            embed = discord.Embed(title='Prefix', description=f'My prefix is:   **{prefix_check(message.guild)}**', color=discord.Color.blue())
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f'Requested by {message.author}', icon_url=message.author.avatar_url)

            await message.delete()
            await message.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(PrefixManagement(bot))
    print('PrefixManagement is loaded')
