import discord
from discord.ext import commands
import mysql.connector
from private.config import mysql_host, mysql_user, mysql_password, mysql_database

mydb = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database)

mycursor = mydb.cursor(buffered=True)


class GuildJoinLeave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """
        Sets the parameters for the guild in the database
        :param guild: The guild that the bot joined
        """
        sql = "INSERT INTO guilds (guild_id, guild_name, welcome_channel) VALUES (%s, %s, %s)"
        val = (guild.id, guild.name, guild.system_channel.id)
        mycursor.execute(sql, val)
        mydb.commit()

        for user in guild.members:
            if user.bot:
                continue
            else:
                sql = "INSERT INTO users (user_id, user_name, guild_id, user_level, user_experience, user_money, " \
                      "`user_is-daily`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                val = (user.id, user.name, guild.id, 0, 0, 100, 1)
                mycursor.execute(sql, val)
                mydb.commit()

        embed = discord.Embed(
            title=f"Hello {guild.name}!",
            description="Thank you for inviting me to your server! I am a bot that is still in development, "
                        "so please be patient with me. If you have any questions, please join me on "
                        "GitHub: https://github.com/Isnubi/FeurBot/",
            color=discord.Color.green())
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.display_avatar.url)
        await guild.system_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        """
        Removes the guild from the database
        :param guild: The guild that the bot left
        """
        sql = "DELETE FROM guilds WHERE guild_id = %s"
        val = (guild.id,)
        mycursor.execute(sql, val)
        mydb.commit()

        sql = "DELETE FROM users WHERE guild_id = %s"
        val = (guild.id,)
        mycursor.execute(sql, val)
        mydb.commit()


async def setup(bot: commands.Bot):
    await bot.add_cog(
        GuildJoinLeave(bot),
        guilds=[discord.Object(id=980975086154682378)])
