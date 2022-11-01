import discord
from discord import app_commands
from discord.ext import commands
import random
import datetime
import mysql.connector
from private.config import mysql_host, mysql_user, mysql_password, mysql_database

mydb = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database)

mycursor = mydb.cursor(buffered=True)


def exp_needed(level):
    """
    Calculates the experience needed to level up with function 50*(level^2.6)
    :param level: The level of the user
    """
    base_exp = 50
    exp_need = base_exp * (pow(level, 2.6))
    return int(exp_need)


class LevelingSystem(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        """
        Check if the message was sent by a user
        Check if the message is a command
        Add experience to the user and check if the user has leveled up
        Update the json file with the new data
        :param message: The message that was sent
        """
        if message.author.bot:
            return
        elif message.content.startswith("/"):
            return
        else:
            sql = "SELECT * FROM users WHERE guild_id = %s AND user_id = %s"
            val = (message.guild.id, message.author.id)
            mycursor.execute(sql, val)
            result = mycursor.fetchone()
            if result is None:
                sql = "INSERT INTO users (guild_id, user_id) VALUES (%s, %s)"
                val = (message.guild.id, message.author.id)
                mycursor.execute(sql, val)
                mydb.commit()
            else:
                sql = "SELECT user_experience, user_level FROM users WHERE guild_id = %s AND user_id = %s"
                val = (message.guild.id, message.author.id)
                mycursor.execute(sql, val)
                result = mycursor.fetchone()
                exp = result[0]
                level = result[1]
                if exp >= exp_needed(level):
                    sql = "UPDATE users SET user_level = %s WHERE guild_id = %s AND user_id = %s"
                    val = (level + 1, message.guild.id, message.author.id)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    sql = "SELECT welcome_channel FROM guilds WHERE guild_id = %s"
                    val = (message.guild.id,)
                    mycursor.execute(sql, val)
                    result = mycursor.fetchone()
                    if result is None:
                        return
                    else:
                        channel = await self.bot.fetch_channel(result[0])
                        await channel.send(f"{message.author.mention} has leveled up to level {level + 1}!")
                else:
                    new_exp = exp + random.randint(1, 10)
                    sql = "UPDATE users SET user_experience = %s WHERE guild_id = %s AND user_id = %s"
                    val = (new_exp, message.guild.id, message.author.id)
                    mycursor.execute(sql, val)
                    mydb.commit()

    @app_commands.command(
        name="rank",
        description="Get your current level")
    @app_commands.describe(
        user="The user to get the level of")
    async def rank(self, interaction: discord.Interaction, user: discord.User = None) -> None:
        """
        Gets the level of the user
        :param interaction: The interaction
        :param user: The user to get the level of
        """
        if user is None:
            user = interaction.user
        sql = "SELECT user_level FROM users WHERE user_id = %s and guild_id = %s"
        val = (user.id, interaction.guild.id)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        if myresult is None:
            await interaction.response.send_message(f"{user.mention} is level 1!")
        else:
            await interaction.response.send_message(f"{user.mention} is level {myresult[0]}!")

    @app_commands.command(
        name="leaderboard",
        description="Get the leaderboard")
    async def leaderboard(self, interaction: discord.Interaction) -> None:
        """
        Gets the leaderboard
        :param interaction: The interaction
        """
        sql = "SELECT user_id, user_level FROM users WHERE guild_id = %s ORDER BY user_experience DESC"
        val = (interaction.guild.id,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        message = f"```\nLeaderboard for {interaction.guild.name}:\n"
        for x in myresult:
            user = await self.bot.fetch_user(x[0])
            message += f"{user.name} is level {x[1]}!\n"
        message += "```"
        await interaction.response.send_message(message)


async def setup(bot: commands.Bot):
    """
    Loads the cog
    :param bot: The bot to load the cog with
    """
    await bot.add_cog(
        LevelingSystem(bot),
        guilds=[discord.Object(id=980975086154682378)])
