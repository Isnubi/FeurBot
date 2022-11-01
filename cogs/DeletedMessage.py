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

        sql = "SELECT system_channel FROM guilds WHERE guild_id = %s"
        val = (message.guild.id,)
        mycursor.execute(sql, val)
        system_channel = mycursor.fetchone()[0]
        if system_channel is None:
            return
        else:
            channel = await self.bot.fetch_channel(system_channel)
            await channel.send(f"**{message.author}** deleted this message:\n"
                               f"{message.content}")

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
        sql = "UPDATE guilds SET system_channel = %s WHERE guild_id = %s"
        val = (channel.id, interaction.guild.id)
        mycursor.execute(sql, val)
        mydb.commit()
        await interaction.response.send_message(f"Set the logs channel to {channel.mention}!")

    @set_logs_channel.error
    async def set_logs_channel_error(self, interaction: discord.Interaction, error: Exception) -> None:
        """
        Error handler for set_logs_channel
        :param interaction: The interaction
        :param error: The error
        """
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message("You don't have permission to use this command", ephemeral=True)

    @app_commands.command(
        name="get_logs_channel",
        description="Get the channel for deleted messages logs")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def get_logs_channel(self, interaction: discord.Interaction) -> None:
        """
        Gets the channel the bot is posting in
        :param interaction: The interaction
        """
        sql = "SELECT system_channel FROM guilds WHERE guild_id = %s"
        val = (interaction.guild.id,)
        mycursor.execute(sql, val)
        mydb.commit()
        channel_id = mycursor.fetchone()[0]
        channel = await self.bot.fetch_channel(channel_id)
        await interaction.response.send_message(f"The logs channel is {channel.mention}!")

    @get_logs_channel.error
    async def get_logs_channel_error(self, interaction: discord.Interaction, error: Exception) -> None:
        """
        Error handler for get_logs_channel
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
