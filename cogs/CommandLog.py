from discord.ext import commands


class CommandLog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener(name='on_command')
    async def on_command(self, ctx):
        print(f'{ctx.command} executed by {ctx.author} on the server {ctx.guild.name} || at {ctx.message.created_at} UTC')


def setup(bot):
    bot.add_cog(CommandLog(bot))
    print('CommandLog is loaded')
