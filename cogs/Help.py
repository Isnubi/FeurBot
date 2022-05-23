from discord.ext import commands
import discord


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):
        embed = discord.Embed(title="**Commands list**", description="List of all the commands available and possible to execute", color=discord.Colour.blue())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

        # Hardware command
        embed.add_field(name="__Hardware__", value="List of all the hardware commands available", inline=False)
        embed.add_field(name="**!cpu**", value="Check the CPU usage", inline=True)
        embed.add_field(name="**!ram**", value="Check the memory usage", inline=True)
        embed.add_field(name="**!temp**", value="Check the temp", inline=True)
        embed.add_field(name="**!ping**", value="Check the bot latency", inline=False)

        # User command
        embed.add_field(name="__User__", value="List of all the user commands available", inline=False)
        embed.add_field(name="**!say** *<something>*", value="Let the bot say something you tell it", inline=True)
        embed.add_field(name="**!pfp** *<@user>*", value="Return the profile picture of mentioned user", inline=True)
        embed.add_field(name="**!roll** *<number>**d**<number>*", value="Roll number of dices with the number of sides you tell it\nYou can\'t roll more than 100 dices\nDices can't have more than 100 sides", inline=False)
        embed.add_field(name="**!userinfo** *<@user>* - [ui, user]", value="Get user informations", inline=False)

        # Admin command
        for role in ctx.message.author.roles:
            if role.name == 'Bot':  # replace with your admin privileges role name
                embed.add_field(name="__Admin__", value="List of all the admin commands available", inline=False)
                embed.add_field(name="**!purge** *<number>*", value="Delete messages in channel", inline=False)

        embed.set_footer(text="Bot made by @isnubi#6221. If you want to contribute, contact him on discord. If you want to report a bug, contact the developer on discord.")

        await ctx.message.delete()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
    print('Help is loaded')
