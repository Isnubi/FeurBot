from discord.ext import commands
import discord
import json


def get_prefix(bot, message):
    """
    Get the prefix for the server the message was sent in
    :param bot: bot object
    :param message: message object
    """
    with open('private/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


class DeletedMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        """
        Logs deleted messages
        :param message: message object
        """
        if message.author.bot:
            return
        if not message.content:
            return
        if message.content.startswith(get_prefix(self.bot, message)):
            return

        with open('private/custom_channel.json', 'r') as f:
            custom_channel = json.load(f)

        if not custom_channel[str(message.guild.id)]:
            return
        if not "logs_channel" in custom_channel[str(message.guild.id)]:
            return
        else:
            logs_channel = message.guild.get_channel(custom_channel[str(message.guild.id)]['logs_channel'])
            await logs_channel.send(f'**{message.author}** deleted message: ```{message.content}```')

    @commands.command(name='set_logs_channel', aliases=['slc'])
    @commands.has_permissions(manage_guild=True)
    async def set_logs_channel(self, ctx, channel: discord.TextChannel):
        """
        Set the channel for logs
        :param ctx: context object
        :param channel: channel object
        """
        with open('private/custom_channel.json', 'r') as f:
            custom_channel = json.load(f)

        custom_channel[str(ctx.guild.id)] = {
            'logs_channel': channel.id
        }

        with open('private/custom_channel.json', 'w') as f:
            json.dump(custom_channel, f, indent=4)

        await ctx.send(f'Logs channel set to {channel.mention}')


def setup(bot):
    bot.add_cog(DeletedMessage(bot))
    print('DeletedMessage is loaded')
