import discord
from discord import app_commands
from discord.ext import commands
import json


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
        if message.content.startswith('/'):
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

    @app_commands.command(
        name="set_logs_channel",
        description="Set a channel for deleted messages logs")
    @app_commands.describe(
        channel="The channel to set")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def set_logs_channel(self, interaction: discord.Interaction, channel: discord.TextChannel) -> None:
        """
        Set the channel for logs
        :param interaction: The interaction
        :param channel: channel object
        """
        with open('private/custom_channel.json', 'r') as f:
            custom_channel = json.load(f)

        custom_channel[str(interaction.guild.id)] = {
            'logs_channel': channel.id
        }

        with open('private/custom_channel.json', 'w') as f:
            json.dump(custom_channel, f, indent=4)

        await interaction.response.send_message(f"Channel set to {channel.mention}")

    @set_logs_channel.error
    async def set_logs_channel_error(self, interaction: discord.Interaction, error: Exception) -> None:
        """
        Error handler for set_logs_channel
        :param interaction: The interaction
        :param error: The error
        """
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message("You don't have permission to use this command", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(
        DeletedMessage(bot),
        guilds=[discord.Object(id=980975086154682378)]
    )
