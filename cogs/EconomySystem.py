from discord.ext import commands
import datetime
import discord
import json


def prefix_check(guild):
    """
    Checks the guild's prefix
    :param guild: The guild to check
    """
    if guild is None:
        return '!'
    try:
        with open('private/prefixes.json', 'r') as f:
            prefixes = json.load(f)
            return prefixes[str(guild.id)]
    except:
        return '!'


class EconomySystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """
        Adds the guild to the economy.json file
        :param guild: Guild to add
        """
        with open("private/economy.json", "r") as f:
            data = json.load(f)
        data[str(guild.id)] = []
        with open("private/economy.json", "w") as f:
            json.dump(data, f, indent=4)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        """
        Removes the guild from the economy.json file
        :param guild: Guild to remove
        """
        with open("private/economy.json", "r") as f:
            data = json.load(f)
        data.pop(str(guild.id))
        with open("private/economy.json", "w") as f:
            json.dump(data, f, indent=4)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """
        Adds the member to the economy.json file
        :param member: Member to add
        """
        with open("private/economy.json", "r") as f:
            data = json.load(f)
        if str(member.guild.id) not in data:
            data[str(member.guild.id)] = []
        if str(member.id) not in data[str(member.guild.id)]:
            current_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            data[str(member.guild.id)][str(member.id)] = {
                "balance": 100,
                "daily_time": current_time,
            }
            with open("private/economy.json", "w") as f:
                json.dump(data, f, indent=4)

    @commands.Cog.listener()
    async def on_member_leave(self, member):
        """
        Removes the member from the economy.json file
        :param member: Member to remove
        """
        with open("private/economy.json", "r") as f:
            data = json.load(f)
        if str(member.guild.id) not in data:
            data[str(member.guild.id)] = []
        if str(member.id) in data[str(member.guild.id)]:
            data[str(member.guild.id)].pop(str(member.id))
        with open("private/economy.json", "w") as f:
            json.dump(data, f, indent=4)

    @commands.command(name="balance", aliases=["bal", "money", "balances"])
    async def balance(self, ctx, user: discord.Member = None):
        """
        Shows the user's balance
        :param ctx: Context
        :param user: User to check
        """
        if user is None:
            user = ctx.author

        with open("private/economy.json", "r") as f:
            data = json.load(f)

        embed = discord.Embed(title="Balance", description='How many coins do you have?', color=discord.Color.blue())
        embed.set_author(name=f"{user.name}'s balance", icon_url=user.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)

        if str(user.id) in data[str(ctx.guild.id)]:
            embed.add_field(name="Balance", value=f"{data[str(ctx.guild.id)][str(user.id)]['balance']} coins")
        else:
            embed.add_field(name="Error", value=f"You are not registered.\nUse `{ctx.prefix}register` to register.")

        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command(name="bank")
    async def bank(self, ctx):
        """
        Command to check the bank of the server
        Leaderboard of money
        :param ctx: The context of the command
        """
        with open("private/economy.json", "r") as f:
            economy = json.load(f)

        embed = discord.Embed(title="Bank", description='Leaderboard of the bank', color=discord.Color.blue())
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.guild.icon_url)

        users = []
        for user in economy[str(ctx.guild.id)]:
            users.append((user, economy[str(ctx.guild.id)][user]["balance"]))
        users = sorted(users, key=lambda x: x[1], reverse=True)

        for i in range(0, len(users), 20):
            for user in users[i:i + 20]:
                embed.add_field(name=f"{self.bot.get_user(int(user[0])).name}",
                                value=f"Balance: {user[1]}", inline=False)
            await ctx.send(embed=embed)
            embed.clear_fields()

        await ctx.message.delete()

    @commands.command(name="register", aliases=["reg", "regist", "registers"])
    async def register(self, ctx):
        """
        Registers the user in the economy.json file if he doesn't have one
        :param ctx: Context of the command
        """
        with open("private/economy.json", "r") as f:
            data = json.load(f)

        embed = discord.Embed(title="Register", description='You\'re not registered yet?', color=discord.Color.blue())
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)

        if str(ctx.author.id) in data[str(ctx.guild.id)]:
            embed.add_field(name="Error", value="You are already registered.")
        else:
            current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            next_daily = datetime.datetime.strptime(current_time, "%d-%m-%Y %H:%M:%S") + datetime.timedelta(days=1)
            data[str(ctx.guild.id)][str(ctx.author.id)] = {
                "balance": 100,
                "daily_time": current_time
            }
            with open("private/economy.json", "w") as f:
                json.dump(data, f, indent=4)
            embed.add_field(name="Success", value=f"You have been registered.\nYour daily reward of 100 coins has been added to your balance.\nYou can claim your daily reward every 24 hours.\nCome back **{next_daily}** to claim your daily reward.")

        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command(name="pay", aliases=["give", "transfer"])
    async def pay(self, ctx, user: discord.Member, amount: int):
        """
        Transfers money from one user to another
        :param ctx: Context of the command
        :param user: User to transfer money to
        :param amount: Amount of money to transfer
        """
        with open("private/economy.json", "r") as f:
            data = json.load(f)

        embed = discord.Embed(title="Pay", description='Pay someone!', color=discord.Color.blue())
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)

        if str(ctx.author.id) in data[str(ctx.guild.id)]:
            if str(user.id) in data[str(ctx.guild.id)]:
                if amount <= data[str(ctx.guild.id)][str(ctx.author.id)]['balance']:
                    data[str(ctx.guild.id)][str(ctx.author.id)]['balance'] -= amount
                    data[str(ctx.guild.id)][str(user.id)]['balance'] += amount
                    with open("private/economy.json", "w") as f:
                        json.dump(data, f, indent=4)
                    embed.add_field(name="Success", value=f"You have successfully transferred {amount} to {user.name}.")
                else:
                    embed.add_field(name="Error", value=f"You don't have enough money to transfer {amount}.")
            else:
                embed.add_field(name="Error", value=f"{user.name} is not registered.")
        else:
            embed.add_field(name="Error", value=f"You are not registered.\nUse `{ctx.prefix}register` to register.")

        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command(name="daily", aliases=["dailycoins"])
    async def daily(self, ctx):
        """
        Gives the user daily coins
        :param ctx: Context of the command
        """
        with open("private/economy.json", "r") as f:
            data = json.load(f)

        embed = discord.Embed(title="Daily", description='Get your daily coins!', color=discord.Color.blue())
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)

        if str(ctx.author.id) in data[str(ctx.guild.id)]:
            current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            last_daily = data[str(ctx.guild.id)][str(ctx.author.id)]['daily_time']
            delta = datetime.datetime.strptime(current_time, "%d-%m-%Y %H:%M:%S") - datetime.datetime.strptime(last_daily, "%d-%m-%Y %H:%M:%S")
            next_daily = datetime.datetime.strptime(current_time, "%d-%m-%Y %H:%M:%S") + datetime.timedelta(days=1)
            if delta.days > 0:
                data[str(ctx.guild.id)][str(ctx.author.id)]['daily_time'] = current_time
                data[str(ctx.guild.id)][str(ctx.author.id)]['balance'] += 100
                with open("private/economy.json", "w") as f:
                    json.dump(data, f, indent=4)
                embed.add_field(name="Success", value=f"You have received 100 coins for being a daily user.\nYou can claim your daily reward every 24 hours.\nCome back **{next_daily}** to claim your daily reward.")
            else:
                embed.add_field(name="Error", value=f"You have already received your daily coins today.\nYou can claim your daily reward every 24 hours.\nCome back **{next_daily}** to claim your daily reward.")
        else:
            embed.add_field(name="Error", value=f"You are not registered.\nUse `{ctx.prefix}register` to register.")

        await ctx.message.delete()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(EconomySystem(bot))
    print("EconomySystem is loaded")
