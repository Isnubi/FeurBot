from discord.ext import commands
import discord
import json


class TalkAs(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the cog
        :param bot: The bot to initialize the cog with.
        """
        self.bot = bot

    @commands.command(name='talkas', aliases=['ta'])
    async def talkas(self, ctx, name, *, message):
        """
        Makes the bot say something as another nickname using webhooks
        :param ctx: The context of where the command was used
        :param name: The nickname to say the message as
        :param message: The message to say
        """

        with open('private/pnj.json', 'r') as f:
            pnj = json.load(f)

        if not str(ctx.message.guild.id) in pnj:
            await ctx.send('This server has no pnj')

        if name in pnj[str(ctx.guild.id)][str(ctx.message.channel.id)]:
            if message == None:
                await ctx.send('Please enter a message')
                return
            webhook = await ctx.channel.create_webhook(name=name)
            await ctx.message.delete()
            await webhook.send(str(message), username=name)
            await webhook.delete()
        else:
            await ctx.send('This pnj does not exist', delete_after=10)
            await ctx.message.delete()
            return

    @commands.command(name='addpnj', aliases=['ap'])
    async def addpnj(self, ctx, name):
        """
        Adds a pnj to the list of pnjs in json file
        :param ctx: The context of where the command was used
        :param name: The nickname to say the message as
        """
        with open('private/pnj.json', 'r') as f:
            pnj = json.load(f)

        if not str(ctx.guild.id) in pnj:
            pnj[str(ctx.guild.id)] = {}
        if not str(ctx.message.channel.id) in pnj[str(ctx.guild.id)]:
            pnj[str(ctx.guild.id)][str(ctx.message.channel.id)] = []

        if name in pnj[str(ctx.guild.id)][str(ctx.message.channel.id)]:
            await ctx.send('This PNJ already exists', delete_after=10)
            return
        else:
            pnj[str(ctx.guild.id)][str(ctx.message.channel.id)].append(name)
            with open('private/pnj.json', 'w') as f:
                json.dump(pnj, f)
            await ctx.send(f'{name} has been added', delete_after=10)
        await ctx.message.delete()

    @commands.command(name='delpnj', aliases=['dp'])
    async def delpnj(self, ctx, name):
        """
        Deletes a pnj from the list of pnjs in json file
        :param ctx: The context of where the command was used
        :param name: The nickname to say the message as
        """
        with open('private/pnj.json', 'r') as f:
            pnj = json.load(f)

        if not str(ctx.guild.id) in pnj:
            pnj[str(ctx.guild.id)] = {}
        if not str(ctx.message.channel.id) in pnj[str(ctx.guild.id)]:
            await ctx.send("Any PNJ in this channel")

        if name in pnj[str(ctx.guild.id)][str(ctx.message.channel.id)]:
            pnj[str(ctx.guild.id)][str(ctx.message.channel.id)].remove(name)
            with open('private/pnj.json', 'w') as f:
                json.dump(pnj, f)
            await ctx.send(f'{name} has been deleted', delete_after=10)
        else:
            await ctx.send("This PNJ doesn't exist for this channel", delete_after=10)
        await ctx.message.delete()

    @commands.command(name='listpnj', aliases=['lp'])
    async def listpnj(self, ctx):
        """
        Lists all the pnjs in the current channel
        :param ctx: The context of where the command was used
        """
        with open('private/pnj.json', 'r') as f:
            pnj = json.load(f)

        if not str(ctx.guild.id) in pnj:
            await ctx.send('This server has no pnj', delete_after=10)

        if not str(ctx.message.channel.id) in pnj[str(ctx.guild.id)]:
            await ctx.send("Any PNJ in this channel", delete_after=10)

        embed = discord.Embed(title="List of PNJs", description=f"In the channel {ctx.channel} in the server {ctx.guild}", color=0x00ff00)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"{self.bot.user.name}", icon_url=self.bot.user.avatar_url)
        for i in pnj[str(ctx.guild.id)][str(ctx.message.channel.id)]:
            embed.add_field(name=i, value="\u200b", inline=False)
        await ctx.author.send(embed=embed)
        await ctx.message.delete()


def setup(bot):
    """
    Initializes the cog
    :param bot: bot object
    """
    bot.add_cog(TalkAs(bot))
    print('TalkAs is loaded')
