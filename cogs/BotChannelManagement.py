import discord
from discord import app_commands
from discord.ext import commands
import mysql.connector
from private.config import mysql_host, mysql_user, mysql_password, mysql_database

mydb = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database)

mycursor = mydb.cursor(buffered=True)


class BotChannelManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="set_welcome_channel",
        description="Set a channel for system channel")
    @app_commands.describe(
        channel="The channel to set")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def set_welcome_channel(self, interaction: discord.Interaction, channel: discord.TextChannel) -> None:
        """
        Sets the channel for the bot to post in
        :param interaction: The interaction
        :param channel: The channel to set the bot to post in
        """
        channel = await self.bot.fetch_channel(channel.id)
        sql = "UPDATE guilds SET welcome_channel = %s WHERE guild_id = %s"
        val = (channel.id, interaction.guild.id)
        mycursor.execute(sql, val)
        mydb.commit()
        await interaction.response.send_message(f"Set the welcome channel to {channel.mention}!")

    @set_welcome_channel.error
    async def set_welcome_channel_error(self, interaction: discord.Interaction, error: Exception) -> None:
        """
        Error handler for set_welcome_channel
        :param interaction: The interaction
        :param error: The error
        """
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message("You don't have permission to use this command", ephemeral=True)

    @app_commands.command(
        name="get_welcome_channel",
        description="Get the channel for system channel")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def get_welcome_channel(self, interaction: discord.Interaction) -> None:
        """
        Gets the channel the bot is posting in
        :param interaction: The interaction
        """
        sql = "SELECT welcome_channel FROM guilds WHERE guild_id = %s"
        val = (str(interaction.guild.id),)
        mycursor.execute(sql, val)
        mydb.commit()
        channel_id = mycursor.fetchone()[0]
        channel = await self.bot.fetch_channel(channel_id)
        await interaction.response.send_message(f"The welcome channel is {channel.mention}!")

    @get_welcome_channel.error
    async def get_welcome_channel_error(self, interaction: discord.Interaction, error: Exception) -> None:
        """
        Error handler for get_welcome_channel
        :param interaction: The interaction
        :param error: The error
        """
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message("You don't have permission to use this command", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(
        BotChannelManagement(bot),
        guilds=[discord.Object(id=980975086154682378)]
    )
