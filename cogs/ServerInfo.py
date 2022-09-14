import discord
from discord import app_commands
from discord.ext import commands


class ServerInfo(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with
        """
        self.bot = bot
        
    @app_commands.command(
        name="serverinfo",
        description="Get the current server information")
    async def serverinfo(self, interaction: discord.Interaction) -> None:
        """
        Displays information about the server
        :param interaction: The interaction to respond to.
        """
        embed = discord.Embed(title=f"{interaction.guild.name} Info", description="Information of this server", color=discord.Colour.blue())
        embed.add_field(name='Owner', value=f"{interaction.guild.owner}", inline=True)
        embed.add_field(name='Verification level', value=f"{interaction.guild.verification_level}", inline=True)
        embed.add_field(name='Created On', value=interaction.guild.created_at.strftime("%b %d %Y"), inline=True)
        embed.add_field(name='Total of roles', value=f"{len(interaction.guild.roles)}", inline=True)

        total_bots, total_online = 0, 0
        for member in interaction.guild.members:
            if member.bot:
                total_bots += 1
            if member.status != discord.Status.offline:
                total_online += 1
        embed.add_field(name='Members', value=f"{len(interaction.guild.members)} members,\n{total_online} online,\n{total_bots} bots, {len(interaction.guild.members) - total_bots} humans", inline=True)

        text_channels = interaction.guild.text_channels
        voice_channels = interaction.guild.voice_channels
        categories = interaction.guild.categories
        total_channels = len(text_channels) + len(voice_channels)
        embed.add_field(name='Total of channels', value=f"{total_channels} channels in total:\n{len(categories)} categories\n{len(text_channels)} text, {len(voice_channels)} voice", inline=True)

        embed.add_field(name='Boost level', value=f"{interaction.guild.premium_tier}", inline=True)
        embed.add_field(name='Boosts number', value=f"{interaction.guild.premium_subscription_count}", inline=True)

        embed.set_footer(text=f'Server name: {interaction.guild.name} | Server ID: {interaction.guild.id}')
        embed.set_thumbnail(url=interaction.guild.icon)
        embed.set_author(name=f'{interaction.user.name}', icon_url=interaction.user.display_avatar.url)

        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(
        ServerInfo(bot),
        guilds=[discord.Object(id=980975086154682378)]
    )
