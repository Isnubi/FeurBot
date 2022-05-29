from discord.ext import commands


class CommandLog(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with.
        """
        self.bot = bot

    @commands.Cog.listener(name='on_command')
    async def on_command(self, ctx):
        """
        Logs the command sent by the user
        :param ctx: The context of the command
        """
        print(f'{ctx.command} executed by {ctx.author} on the server {ctx.guild.name} || at {ctx.message.created_at} UTC')


def setup(bot):
    """
    Initializes the cog
    :param bot: bot object
    """
    bot.add_cog(CommandLog(bot))
    print('CommandLog is loaded')
