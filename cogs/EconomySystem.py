import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import datetime
import mysql.connector
from private.config import mysql_host, mysql_user, mysql_password, mysql_database

mydb = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database)

mycursor = mydb.cursor(buffered=True)


def seconds_until_task(hours, minutes):
    given_time = datetime.time(hours, minutes)
    now = datetime.datetime.now()
    future_exec = datetime.datetime.combine(now, given_time)
    if (future_exec - now).days < 0:
        future_exec = datetime.datetime.combine(now + datetime.timedelta(days=1), given_time)
    return (future_exec - now).total_seconds()


async def daily_reset():
    """
    Reset the daily coin status in the database every day
    """
    while True:
        await asyncio.sleep(seconds_until_task(0, 0))
        try:
            sql = "UPDATE users SET `user_is-daily` = 0"
            mycursor.execute(sql)
            mydb.commit()
        except Exception as e:
            print(e)
            pass
        print(f"Daily reset {datetime.datetime.now()}")
        await asyncio.sleep(60)


class EconomySystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.loop.create_task(daily_reset())

    @app_commands.command(
        name="balance",
        description="Get your balance")
    @app_commands.describe(
        user="The user to get the balance of")
    async def balance(self, interaction: discord.Interaction, user: discord.User = None) -> None:
        """
        Gets the balance of a user
        :param interaction: The interaction
        :param user: The user to get the balance of
        """
        if user is None:
            user = interaction.user
        sql = "SELECT user_money FROM users WHERE user_id = %s and guild_id = %s"
        val = (user.id, interaction.guild.id)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        if result is None:
            await interaction.response.send_message(f"{user.mention} has 0 coins!")
        else:
            await interaction.response.send_message(f"{user.mention} has {result[0]} coins!")

    @app_commands.command(
        name="bank",
        description="Get the most rich users")
    async def bank(self, interaction: discord.Interaction) -> None:
        """
        Gets the most rich users
        :param interaction: The interaction
        """
        sql = "SELECT user_id, user_money FROM users WHERE guild_id = %s ORDER BY user_money DESC LIMIT 10"
        val = (interaction.guild.id,)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        if result is None:
            await interaction.response.send_message("There is no user in the bank!")
        else:
            embed = discord.Embed(
                title="Bank",
                description="The 10 most rich users",
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow()
            )
            for row in result:
                user = await self.bot.fetch_user(row[0])
                embed.add_field(
                    name=f"{user.name}#{user.discriminator}",
                    value=f"{row[1]} coins",
                    inline=False
                )
            await interaction.response.send_message(embed=embed)

    @app_commands.command(
        name="pay",
        description="Pay a user")
    @app_commands.describe(
        user="The user to pay",
        amount="The amount to pay")
    async def pay(self, interaction: discord.Interaction, user: discord.User, amount: int) -> None:
        """
        Pay a user
        :param interaction: The interaction
        :param user: The user to pay
        :param amount: The amount to pay
        """
        if user == interaction.user:
            await interaction.response.send_message("You can't pay yourself!")
        else:
            sql = "SELECT user_money FROM users WHERE user_id = %s and guild_id = %s"
            val = (interaction.user.id, interaction.guild.id)
            mycursor.execute(sql, val)
            result = mycursor.fetchone()
            if result is None:
                await interaction.response.send_message("You don't have any coins!")
            elif result[0] < amount:
                await interaction.response.send_message("You don't have enough coins!")
            else:
                sql = "UPDATE users SET user_money = user_money - %s WHERE user_id = %s and guild_id = %s"
                val = (amount, interaction.user.id, interaction.guild.id)
                mycursor.execute(sql, val)
                mydb.commit()
                sql = "UPDATE users SET user_money = user_money + %s WHERE user_id = %s and guild_id = %s"
                val = (amount, user.id, interaction.guild.id)
                mycursor.execute(sql, val)
                mydb.commit()
                await interaction.response.send_message(f"You paid {user.mention} {amount} coins!")

    @app_commands.command(
        name="daily",
        description="Get your daily coins")
    async def daily(self, interaction: discord.Interaction) -> None:
        """
        Gets the daily coins
        :param interaction: The interaction
        """
        sql = "SELECT `user_is-daily` FROM users WHERE user_id = %s and guild_id = %s"
        val = (interaction.user.id, interaction.guild.id)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        if result is None or result[0] == 0:
            sql = "UPDATE users SET user_money = user_money + 100, " \
                  "`user_is-daily` = 1 WHERE user_id = %s and guild_id = %s"
            val = (interaction.user.id, interaction.guild.id)
            mycursor.execute(sql, val)
            mydb.commit()
            await interaction.response.send_message("You got your 100 daily coins!")
        else:
            await interaction.response.send_message("You already got your daily coins!")


async def setup(bot: commands.Bot):
    await bot.add_cog(
        EconomySystem(bot),
        guilds=[discord.Object(id=980975086154682378)]
    )
