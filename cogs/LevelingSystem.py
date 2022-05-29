from discord.ext import commands
import discord
import json
import random
import datetime


class LevelingSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def add_experience(self, json_file, guild_id, user_id, experience):
        json_file[str(guild_id)][str(user_id)]["experience"] += experience

    def level_up(self, json_file, guild_id, user_id):
        experience = json_file[str(guild_id)][str(user_id)]["experience"]
        level = json_file[str(guild_id)][str(user_id)]["level"]
        if experience >= 100:
            json_file[str(guild_id)][str(user_id)]["experience"] -= 100
            json_file[str(guild_id)][str(user_id)]["level"] += 1
            return
        else:
            return

    def add_last_message(self, json_file, guild_id, user_id, message_timestamp):
        json_file[str(guild_id)][str(user_id)]["last_message"] = message_timestamp
        return

    def update_data(self, json_file, guild_id, user_id):
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
        if message.author.bot:
            return
        else:
            if message.content.startswith("!"):
                return
            else:
                with open("private/leveling.json", "r") as f:
                    leveling = json.load(f)

                self.update_data(leveling, message.guild.id, message.author.id)

                last_message = leveling[str(message.guild.id)][str(message.author.id)]["last_message"]
                current_time = datetime.datetime.utcnow().strftime("%d-%m-%Y %H:%M:%S")
                delta = datetime.datetime.strptime(current_time, "%d-%m-%Y %H:%M:%S") - datetime.datetime.strptime(last_message, "%d-%m-%Y %H:%M:%S")
                print(delta.seconds)
                if delta.seconds < 5:
                    return
                else:
                    message_timestamp = message.created_at.strftime("%d-%m-%Y %H:%M:%S")
                    self.add_experience(leveling, message.guild.id, message.author.id, random.randint(1, 5))
                    self.level_up(leveling, message.guild.id, message.author.id)
                    self.add_last_message(leveling, message.guild.id, message.author.id, message_timestamp)

                with open("private/leveling.json", "w") as f:
                    json.dump(leveling, f, indent=4)

    @commands.command(name="level", aliases=["lvl", "rank"])
    async def level(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author
        with open("private/leveling.json", "r") as f:
            leveling = json.load(f)

        lvl = leveling[str(ctx.guild.id)][str(user.id)]["level"]
        exp = leveling[str(ctx.guild.id)][str(user.id)]["experience"]

        embed = discord.Embed(title=f"{user.name}'s Level", description=f"{user.mention} is level {lvl} with {exp} experience.", color=discord.Color.blue())
        embed.set_author(name=user.name, icon_url=user.avatar_url)

        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command(name="leaderboard")
    async def leaderboard(self, ctx):
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
        for user in users:
            embed.add_field(name=f"{self.bot.get_user(int(user[0])).name}", value=f"Level: {user[1]}\nExperience: {user[2]}", inline=False)

        await ctx.message.delete()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(LevelingSystem(bot))
    print("LevelingSystem is loaded")
