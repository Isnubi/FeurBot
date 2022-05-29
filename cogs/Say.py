from discord.ext import commands


class Say(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with
        """
        self.bot = bot

    @commands.command(name="say")
    async def say(self, ctx, *, message):
        """
        Let the bot say something for you
        :param ctx: The context of the command
        :param message: The message to say
        """
        send_message = ctx.message
        await send_message.delete()
        await ctx.send(f"{message}")


def setup(bot):
    """
    Initializes the cog
    :param bot: bot object
    """
    bot.add_cog(Say(bot))
    print("Say is loaded")
