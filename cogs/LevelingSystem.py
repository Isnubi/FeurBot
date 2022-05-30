from discord.ext import commands
import discord
import json
import random
import datetime


class LevelingSystem(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with
        """
        self.bot = bot

    def exp_needed(self, level):
        """
        Calculates the experience needed to level up with function 50*(level^2.6)
        :param level: The level of the user
        """
        base_exp = 50
        exp_needed = base_exp * (pow(level, 2.6))
        return int(exp_needed)

    def add_experience(self, json_file, guild_id, user_id, experience):
        """
        Adds experience to the user
        :param json_file: The json file to add the experience to
        :param guild_id: The guild id of the guild
        :param user_id: The user id of the user
        :param experience: The amount of experience to add
        """
        json_file[str(guild_id)][str(user_id)]["experience"] += experience

    def level_up(self, json_file, guild_id, user_id, message):
        """
        Checks if the user has leveled up
        :param json_file: The json file to check the user's level in
        :param guild_id: The guild id of the guild
        :param user_id: The user id of the user
        :param message: The message that was sent
        """
        experience = json_file[str(guild_id)][str(user_id)]["experience"]
        level = json_file[str(guild_id)][str(user_id)]["level"]
        if experience >= self.exp_needed(level):
            json_file[str(guild_id)][str(user_id)]["experience"] -= self.exp_needed(level)
            json_file[str(guild_id)][str(user_id)]["level"] += 1

            embed = discord.Embed(title="Level up!", description=f"{message.author.mention} has leveled up to level {level + 1}!", color=discord.Color.blue())
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f"{message.author.name}'s Level", icon_url=message.author.avatar_url)
            return embed
        else:
            return

    def add_last_message(self, json_file, guild_id, user_id, message_timestamp):
        """
        Adds the last message timestamp to the user data in the json file
        :param json_file: The json file to add the last message to
        :param guild_id: The guild id of the guild
        :param user_id: The user id of the user
        :param message_timestamp: The timestamp of the message
        """
        json_file[str(guild_id)][str(user_id)]["last_message"] = message_timestamp
        return

    def update_data(self, json_file, guild_id, user_id):
        """
        Updates the json file with the new data when the user or the guild is unknwon
        :param json_file: The json file to update
        :param guild_id: The guild id of the guild
        :param user_id: The user id of the user
        """
        if not str(guild_id) in json_file:
            json_file[str(guild_id)] = {}
        if not str(user_id) in json_file[str(guild_id)]:
            json_file[str(guild_id)][str(user_id)] = {
                "experience": 0,
                "level": 1,
                "last_message": "00-00-0000 00:00:00"
            }

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
        else:
            with open("private/prefixes.json", "r") as f:
                prefixes = json.load(f)
            if str(message.guild.id) in prefixes:
                prefix = prefixes[str(message.guild.id)]
            else:
                prefix = "!"
            if message.content.startswith(prefix):
                return
            else:
                with open("private/leveling.json", "r") as f:
                    leveling = json.load(f)

                self.update_data(leveling, message.guild.id, message.author.id)

                last_message = leveling[str(message.guild.id)][str(message.author.id)]["last_message"]
                current_time = datetime.datetime.utcnow().strftime("%d-%m-%Y %H:%M:%S")
                delta = datetime.datetime.strptime(current_time, "%d-%m-%Y %H:%M:%S") - datetime.datetime.strptime(last_message, "%d-%m-%Y %H:%M:%S")
                if delta.seconds < 5:
                    return
                else:
                    message_timestamp = message.created_at.strftime("%d-%m-%Y %H:%M:%S")
                    self.add_experience(leveling, message.guild.id, message.author.id, random.randint(1, 5))
                    levelup = self.level_up(leveling, message.guild.id, message.author.id, message)
                    if levelup:
                        await message.channel.send(embed=levelup)
                    self.add_last_message(leveling, message.guild.id, message.author.id, message_timestamp)

                with open("private/leveling.json", "w") as f:
                    json.dump(leveling, f, indent=4)

    @commands.command(name="level", aliases=["lvl", "rank"])
    async def level(self, ctx, user: discord.Member = None):
        """
        Command to check the level of a user
        :param ctx: The context of the command
        :param user: The user to check the level of
        """
        if user is None:
            user = ctx.author
        with open("private/leveling.json", "r") as f:
            leveling = json.load(f)

        lvl = leveling[str(ctx.guild.id)][str(user.id)]["level"]
        exp = leveling[str(ctx.guild.id)][str(user.id)]["experience"]

        embed = discord.Embed(title=f"{user.name}'s Level", description=f"{user.mention} is level {lvl} with {exp} experience.", color=discord.Color.blue())
        embed.add_field(name="Experience Needed to Level Up", value=self.exp_needed(lvl), inline=False)
        embed.set_author(name=user.name, icon_url=user.avatar_url)

        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command(name="leaderboard")
    async def leaderboard(self, ctx):
        """
        Command to check the leaderboard of the server
        :param ctx: The context of the command
        """
        with open("private/leveling.json", "r") as f:
            leveling = json.load(f)

        embed = discord.Embed(title="Leveling Leaderboard", description="", color=discord.Color.blue())
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.guild.icon_url)

        users = []
        for user in leveling[str(ctx.guild.id)]:
            lvl = leveling[str(ctx.guild.id)][str(user)]["level"]
            exp = leveling[str(ctx.guild.id)][str(user)]["experience"]
            users.append((user, lvl, exp))
        users = sorted(sorted(users, key=lambda x: x[2], reverse=True), key=lambda x: x[1], reverse=True)

        for i in range(0, len(users), 20):
            for user in users[i:i+20]:
                embed.add_field(name=f"{self.bot.get_user(int(user[0])).name}", value=f"Level: {user[1]}\nExperience: {user[2]}", inline=False)
            await ctx.send(embed=embed)
            embed.clear_fields()

        await ctx.message.delete()


def setup(bot):
    """
    Initializes the cog
    :param bot: bot object
    """
    bot.add_cog(LevelingSystem(bot))
    print("LevelingSystem is loaded")
