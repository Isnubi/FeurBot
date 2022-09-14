import discord
from discord import app_commands
from discord.ext import commands
import json


class BotChannelManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="set_channel",
        description="Set a channel for system channel")
    @app_commands.describe(
        channel="The channel to set")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def set_channel(self, interaction: discord.Interaction, channel: discord.TextChannel) -> None:
        """
        Sets the channel for the bot to post in
        :param interaction: The interaction
        :param channel: The channel to set the bot to post in
        """
        channel = await self.bot.fetch_channel(channel.id)
        with open('private/custom_channel.json', 'r') as f:
            data = json.load(f)

        data[str(interaction.guild.id)]["channel"] = str(channel.id)

        with open('private/custom_channel.json', 'w') as f:
            json.dump(data, f, indent=4)

        await interaction.response.send_message(f"Channel set to {channel.mention}")

    @app_commands.command(
        name="get_channel",
        description="Get the channel for system channel")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def get_channel(self, interaction: discord.Interaction) -> None:
        """
        Gets the channel the bot is posting in
        :param interaction: The interaction
        """
        with open('private/custom_channel.json', 'r') as f:
            data = json.load(f)

        if not str(interaction.guild.id) in data:
            await interaction.response.send_message("No channel set")
        else:
            channel = await self.bot.fetch_channel(int(data[str(interaction.guild.id)]["channel"]))
            await interaction.response.send_message(f"Channel set to {channel.mention}")

    @app_commands.command(
        name="reset_channel",
        description="Reset the channel for system channel")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def reset_channel(self, interaction: discord.Interaction) -> None:
        """
        Resets the channel for the bot to post in
        :param interaction: The interaction
        """
        with open('private/custom_channel.json', 'r') as f:
            data = json.load(f)

        if not str(interaction.guild.id) in data:
            data[str(interaction.guild.id)] = {"channel": str(interaction.guild.system_channel.id)}
        else:
            data[str(interaction.guild.id)]["channel"] = str(interaction.guild.system_channel.id)

        with open('private/custom_channel.json', 'w') as f:
            json.dump(data, f, indent=4)

        await interaction.response.send_message(f"Channel reset to {interaction.guild.system_channel.mention}")

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


async def setup(bot: commands.Bot):
    await bot.add_cog(
        BotChannelManagement(bot),
        guilds=[discord.Object(id=980975086154682378)]
    )
