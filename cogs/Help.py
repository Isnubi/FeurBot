import discord
from discord import app_commands
from discord.ext import commands
import asyncio


class Help(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with
        """
        self.bot = bot
        
    @app_commands.command(
        name="help",
        description="Get the help menu of the bot")
    @app_commands.describe(
        page_number="The page number of the help menu (from 1 to 10)"
    )
    async def help(self, interaction: discord.Interaction, page_number: int) -> None:
        """
        Sends the help menu in an embed message with pages
        :param interaction: The interaction to respond to
        :param page_number: The page number of the help menu
        """
        user_commands = discord.Embed(title="**Commands list - 1/9**",
                                      description="List of all the commands available and possible to execute",
                                      color=discord.Colour.blue())
        user_commands.add_field(name='__User__', value='List of all the user commands available', inline=False)
        user_commands.add_field(name=f"**/profilepicture** *<@user>*", value="Return the profile picture of mentioned user",
                                inline=True)
        user_commands.add_field(name=f"**/roll** *<number>**d**<number>*",
                                value="Roll number of dices with the number of sides you tell it\n"
                                      "You can\'t roll more than 100 dices\nDices can't have more than 100 sides",
                                inline=False)
        user_commands.add_field(name=f"**/userinfo** *<@user>* - [ui, user]", value="Get user information", inline=True)
        user_commands.add_field(name=f"**/serverinfo** - [si, server]", value="Get server information", inline=True)
        user_commands.add_field(name=f"**/botinfo** - [bi, bot]", value="Get bot information", inline=True)
        user_commands.set_author(name=interaction.user.name, icon_url=interaction.user.display_avatar.url)
        user_commands.set_footer(text="Bot made by @isnubi#6221. If you want to contribute, contact him on discord. "
                                      "If you want to report a bug, contact the developer on discord.")

        fun_commands = discord.Embed(title="**Commands list - 2/9**",
                                     description="List of all the commands available and possible to execute",
                                     color=discord.Colour.blue())
        fun_commands.add_field(name="__Fun__", value="List of all the fun commands available", inline=False)
        # fun_commands.add_field(name=f"**/quiz** -[q]", value="Play a quiz", inline=True)
        fun_commands.add_field(name=f"**/gif**", value="Get a random gif from giphy", inline=True)
        fun_commands.set_author(name=interaction.user.name, icon_url=interaction.user.display_avatar.url)
        fun_commands.set_footer(text="Bot made by @isnubi#6221. If you want to contribute, contact him on discord. "
                                     "If you want to report a bug, contact the developer on discord.")

        talk_as_commands = discord.Embed(title="**Commands list - 3/9**",
                                         description="List of all the commands available and possible to execute",
                                         color=discord.Colour.blue())
        talk_as_commands.add_field(name="__Talk as__", value="List of all the commands available", inline=False)
        talk_as_commands.add_field(name=f"**/talkas** *\"<pnj name>\"* *<message>* - [ta]", value="Talk as PNJ",
                                   inline=True)
        talk_as_commands.add_field(name=f"**/addpnj** *\"<pnj name>\"* - [ap]", value="Add a PNJ for the channel",
                                   inline=True)
        talk_as_commands.add_field(name=f"**/delpnj** *\"<pnj name>\"* - [dp]", value="Delete a PNJ for the channel",
                                   inline=True)
        talk_as_commands.add_field(name=f"**/listpnj** - [lp]",
                                   value="List all the PNJs for the channel\nMessage send in private message",
                                   inline=True)
        talk_as_commands.set_author(name=interaction.user.name, icon_url=interaction.user.display_avatar.url)
        talk_as_commands.set_footer(text="Bot made by @isnubi#6221. If you want to contribute, contact him on discord. "
                                         "If you want to report a bug, contact the developer on discord.")

        economy_commands = discord.Embed(title="**Commands list - 4/9**",
                                         description="List of all the commands available and possible to execute",
                                         color=discord.Colour.blue())
        economy_commands.add_field(name="__Economy__", value="List of all the economy commands available", inline=False)
        economy_commands.add_field(name=f"**/register** - [r]", value="Register your account if you don't have any one",
                                   inline=True)
        economy_commands.add_field(name=f"**/balance** - [b]", value="Get your balance", inline=True)
        economy_commands.add_field(name=f"**/daily** - [d]", value="Get your daily reward every 24 hours", inline=True)
        economy_commands.add_field(name=f"**/pay** *<@user>* *<amount>*", value="Pay someone money", inline=True)

        leveling_commands = discord.Embed(title="**Commands list - 5/9**",
                                          description="List of all the commands available and possible to execute",
                                          color=discord.Colour.blue())
        leveling_commands.add_field(name="__Leveling__", value="List of all the leveling commands available",
                                    inline=False)
        leveling_commands.add_field(name=f"**/level** *<@user>*", value="Get the level of the mentioned user",
                                    inline=True)
        leveling_commands.add_field(name=f"**/leaderboard**", value="Get the leaderboard", inline=True)
        leveling_commands.set_author(name=interaction.user.name, icon_url=interaction.user.display_avatar.url)
        leveling_commands.set_footer(text="Bot made by @isnubi#6221. If you want to contribute, "
                                          "contact him on discord. "
                                          "If you want to report a bug, contact the developer on discord.")
        
        music_commands = discord.Embed(title="**Commands list - 6/9**",
                                       description="List of all the commands available and possible to execute",
                                       color=discord.Colour.blue())
        music_commands.add_field(name="__Music__", value="List of all the music commands available", inline=False)
        music_commands.add_field(name=f"**/join**", value="Join the channel you're in", inline=True)
        music_commands.add_field(name=f"**/play** *<url>*", value="Play a song from youtube", inline=True)
        music_commands.add_field(name=f"**/pause**", value="Pause the current song", inline=True)
        music_commands.add_field(name=f"**/resume**", value="Resume the current song", inline=True)
        music_commands.add_field(name=f"**/stop**", value="Stop the music", inline=True)
        music_commands.add_field(name=f"**/volume** *<number>*", value="Change the volume of the music", inline=True)
        music_commands.add_field(name=f"**/leave**", value="Leave the channel you're in", inline=True)
        music_commands.set_author(name=interaction.user.name, icon_url=interaction.user.display_avatar.url)
        music_commands.set_footer(text="Bot made by @isnubi#6221. If you want to contribute, contact him on discord. "
                                       "If you want to report a bug, contact the developer on discord.")
        
        moderation_commands = discord.Embed(title="**Commands list - 7/9**",
                                            description="List of all the commands available and possible to execute",
                                            color=discord.Colour.blue())
        moderation_commands.add_field(name="__Moderation__",
                                      value="List of all the moderation commands available\nThese commands are limited "
                                            "for user with privileges in order of the command", inline=False)
        moderation_commands.add_field(name=f"**/purge** *<number>*", value="Delete messages in channel", inline=True)
        moderation_commands.add_field(name=f"**/kick** *<@user>*", value="Kick the mentioned user", inline=True)
        moderation_commands.add_field(name=f"**/ban** *<@user>*", value="Ban the mentioned user", inline=True)
        moderation_commands.add_field(name=f"**/banlist**", value="List of all the banned users", inline=True)
        moderation_commands.add_field(name=f"**/unban** *<userid>*", value="Unban the mentioned user", inline=True)
        moderation_commands.add_field(name=f"**/mute** *<@user>*", value="Mute the mentioned user", inline=True)
        moderation_commands.add_field(name=f"**/unmute** *<@user>*", value="Unmute the mentioned user", inline=True)
        moderation_commands.set_author(name=interaction.user.name, icon_url=interaction.user.display_avatar.url)
        moderation_commands.set_footer(text="Bot made by @isnubi#6221. If you want to contribute, "
                                            "contact him on discord. If you want to report a bug, contact the "
                                            "developer on discord.")

        systemchannel_commands = discord.Embed(title="**Commands list - 8/9**",
                                               description="List of all the commands available and possible to execute",
                                               color=discord.Colour.blue())
        systemchannel_commands.add_field(name="__System channel__",
                                         value="List of all the system channel commands available\nThese commands are "
                                               "limited for user with **manage channel** permission", inline=False)
        systemchannel_commands.add_field(name=f"**/setchannel** *<channel>*",
                                         value="Set the channel where the bot will send the messages", inline=True)
        systemchannel_commands.add_field(name=f"**/resetchannel**",
                                         value="Reset the channel where the bot will send the messages", inline=True)
        systemchannel_commands.add_field(name=f"**/set_logs_channel** *<channel>*",
                                         value="Set the channel where the bot will send the logs of deleted messages",
                                         inline=True)
        systemchannel_commands.set_author(name=interaction.user.name, icon_url=interaction.user.display_avatar.url)
        systemchannel_commands.set_footer(text="Bot made by @isnubi#6221. If you want to contribute, "
                                               "contact him on discord. If you want to report a bug, contact the "
                                               "developer on discord.")

        hardware_commands = discord.Embed(title="**Commands list - 9/9**",
                                          description="List of all the commands available and possible to execute",
                                          color=discord.Colour.blue())
        hardware_commands.add_field(name="__Hardware__", value="List of all the hardware commands available",
                                    inline=False)
        hardware_commands.add_field(name=f"**/ping**", value="Get the latency of the bot", inline=True)
        hardware_commands.add_field(name=f"**/cpu**", value="Get the CPU usage of the bot", inline=True)
        hardware_commands.add_field(name=f"**/ram**", value="Get the RAM usage of the bot", inline=True)
        hardware_commands.set_author(name=interaction.user.name, icon_url=interaction.user.display_avatar.url)
        hardware_commands.set_footer(text="Bot made by @isnubi#6221. If you want to contribute, "
                                          "contact him on discord. If you want to report a bug, contact the "
                                          "developer on discord.")

        pages = [user_commands, fun_commands, talk_as_commands, economy_commands, leveling_commands, music_commands,
                 moderation_commands, systemchannel_commands, hardware_commands]

        await interaction.response.send_message(embed=pages[page_number - 1], ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(
        Help(bot),
        guilds=[discord.Object(id=980975086154682378)]
    )
