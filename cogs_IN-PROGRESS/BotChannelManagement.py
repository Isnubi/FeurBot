from discord.ext import commands
import discord
import json


class BotChannelManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='setchannel')
    @commands.has_permissions(manage_channels=True)
    async def setchannel(self, ctx, channel: discord.TextChannel):
        """
        Sets the channel for the bot to post in
        :param ctx: The context of the command
        :param channel: The channel to set the bot to post in
        """
        channel = await self.bot.fetch_channel(channel.id)
        with open('private/custom_channel.json', 'r') as f:
            data = json.load(f)

        data[str(ctx.guild.id)]["channel"] = str(channel.id)

        with open('private/custom_channel.json', 'w') as f:
            json.dump(data, f, indent=4)

        await ctx.send(f'Set channel to {channel.mention}')

    @commands.command(name='getchannel')
    @commands.has_permissions(manage_channels=True)
    async def getchannel(self, ctx):
        """
        Gets the channel the bot is posting in
        :param ctx: The context of the command
        """
        with open('private/custom_channel.json', 'r') as f:
            data = json.load(f)

        if not str(ctx.guild.id) in data:
            await ctx.send(f'No channel set for this guild')
        else:
            channel = await self.bot.fetch_channel(int(data[str(ctx.guild.id)]["channel"]))
            await ctx.send(f'The channel is {channel.mention}')

    @commands.command(name='resetchannel')
    @commands.has_permissions(manage_channels=True)
    async def resetchannel(self, ctx):
        """
        Resets the channel for the bot to post in
        :param ctx: The context of the command
        """
        with open('private/custom_channel.json', 'r') as f:
            data = json.load(f)

        if not str(ctx.guild.id) in data:
            data[str(ctx.guild.id)] = {"channel": str(ctx.guild.system_channel.id)}
        else:
            data[str(ctx.guild.id)]["channel"] = str(ctx.guild.system_channel.id)

        with open('private/custom_channel.json', 'w') as f:
            json.dump(data, f, indent=4)

        await ctx.send(f'Reset channel to {ctx.guild.system_channel.mention}')

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """
        Sets the channel for the bot to post in on join to the system chanel of the guild
        :param guild: The guild that the bot joined
        """
        with open('private/custom_channel.json', 'r') as f:
            data = json.load(f)

        data[str(guild.id)] = {"channel": str(guild.system_channel.id)}

        with open('private/custom_channel.json', 'w') as f:
            json.dump(data, f, indent=4)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        """
        Removes the guild from the custom channel file
        :param guild: The guild that the bot left
        """
        with open('private/custom_channel.json', 'r') as f:
            data = json.load(f)

        del data[str(guild.id)]

        with open('private/custom_channel.json', 'w') as f:
            json.dump(data, f, indent=4)


def setup(bot):
    bot.add_cog(BotChannelManagement(bot))
    print('BotChannelManagement is loaded')
