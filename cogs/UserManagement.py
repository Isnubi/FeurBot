import discord
from discord import app_commands
from discord.ext import commands


class UserManagement(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with
        """
        self.bot = bot

    @app_commands.command(name="mute", description="Mute a user")
    @app_commands.describe(
        user="The user to mute"
    )
    @app_commands.checks.has_permissions(manage_roles=True)
    async def mute(self, interaction: discord.Interaction, user: discord.Member):
        """
        Mutes a user
        :param interaction: The interaction that triggered the command
        :param user: The user to mute
        """
        if user.voice is None:
            await interaction.response.send_message("The user is not in a voice channel", ephemeral=True)
            return
        await user.edit(mute=True)
        await interaction.response.send_message(f"Muted {user.mention}")

    @mute.error
    async def mute_error(self, interaction: discord.Interaction, error: Exception):
        """
        Error handler for mute
        :param interaction: The interaction that triggered the command
        :param error: The error
        """
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message("You don't have permission to use this command", ephemeral=True)

    @app_commands.command(name="unmute", description="Unmute a user")
    @app_commands.describe(
        user="The user to unmute")
    @app_commands.checks.has_permissions(manage_roles=True)
    async def unmute(self, interaction: discord.Interaction, user: discord.Member):
        """
        Unmutes a user
        :param interaction: The interaction that triggered the command
        :param user: The user to unmute
        """
        if user.voice is None:
            await interaction.response.send_message("The user is not in a voice channel", ephemeral=True)
            return
        await user.edit(mute=False)
        await interaction.response.send_message(f"Unmuted {user.mention}")

    @unmute.error
    async def unmute_error(self, interaction: discord.Interaction, error: Exception):
        """
        Error handler for unmute
        :param interaction: The interaction that triggered the command
        :param error: The error
        """
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message("You don't have permission to use this command", ephemeral=True)

    @app_commands.command(name="kick", description="Kick a user")
    @app_commands.describe(
        user="The user to kick",
        reason="The reason for the kick")
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick(self, interaction: discord.Interaction, user: discord.Member, reason: str):
        """
        Kicks a user
        :param interaction: The interaction that triggered the command
        :param user: The user to kick
        :param reason: The reason for the kick
        """
        await user.kick(reason=reason)
        await interaction.response.send_message(f"Kicked {user.mention}")

    @kick.error
    async def kick_error(self, interaction: discord.Interaction, error: Exception):
        """
        Error handler for kick
        :param interaction: The interaction that triggered the command
        :param error: The error
        """
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message("You don't have permission to use this command", ephemeral=True)

    @app_commands.command(name="ban", description="Ban a user")
    @app_commands.describe(
        user="The user to ban",
        reason="The reason for the ban")
    @app_commands.checks.has_permissions(ban_members=True)
    async def ban(self, interaction: discord.Interaction, user: discord.Member, reason: str):
        """
        Bans a user
        :param interaction: The interaction that triggered the command
        :param user: The user to ban
        :param reason: The reason for the ban
        """
        await user.ban(reason=reason)
        await interaction.response.send_message(f"Banned {user.mention}")

    @ban.error
    async def ban_error(self, interaction: discord.Interaction, error: Exception):
        """
        Error handler for ban
        :param interaction: The interaction that triggered the command
        :param error: The error
        """
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message("You don't have permission to use this command", ephemeral=True)

    @app_commands.command(name="banlist", description="Get the ban list")
    @app_commands.checks.has_permissions(ban_members=True)
    async def banlist(self, interaction: discord.Interaction):
        """
        Gets the ban list
        :param interaction: The interaction that triggered the command
        """
        bans = await interaction.guild.bans()
        await interaction.response.send_message(f"Ban list: {', '.join([str(ban.user) for ban in bans])}")

    @banlist.error
    async def banlist_error(self, interaction: discord.Interaction, error: Exception):
        """
        Error handler for banlist
        :param interaction: The interaction that triggered the command
        :param error: The error
        """
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message("You don't have permission to use this command", ephemeral=True)

    @app_commands.command(name="unban", description="Unban a user")
    @app_commands.describe(user="The user to unban")
    @app_commands.checks.has_permissions(ban_members=True)
    async def unban(self, interaction: discord.Interaction, user: discord.User):
        """
        Unbans a user
        :param interaction: The interaction that triggered the command
        :param user: The user to unban
        """
        bans = await interaction.guild.bans()
        for ban in bans:
            if ban.user == user:
                await interaction.guild.unban(ban.user)
                await interaction.response.send_message(f"Unbanned {user.mention}")
                return
            else:
                await interaction.response.send_message(f"{user.mention} is not banned", ephemeral=True)
                return
        await interaction.response.send_message(f"{user.mention} is not banned", ephemeral=True)

    @unban.error
    async def unban_error(self, interaction: discord.Interaction, error: Exception):
        """
        Error handler for unban
        :param interaction: The interaction that triggered the command
        :param error: The error
        """
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message("You don't have permission to use this command", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(
        UserManagement(bot),
        guilds=[discord.Object(id=980975086154682378)])
