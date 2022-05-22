from discord.ext import commands


class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, message):
        send_message = ctx.message
        await send_message.delete()
        await ctx.send(f"{message}")


def setup(bot):
    bot.add_cog(Say(bot))
