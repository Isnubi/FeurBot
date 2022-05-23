from discord.ext import commands
import re
import random


class QuoiFeur(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        out = ((re.sub(r'[^\w\s]', '', message.content)).rstrip())
        end = out[len(out) - 4:len(out)]
        if end == "quoi" or end == "Quoi":
            if random.randint(0, 100) < 25:
                quoi_answer = ['chi!', 'drilatère!', 'ffage!', 'feuse!', 'ffure!', 'ffer!', 'driceps!', 'tuor!',
                               'druplé!', 'artz!', 'druple!', 'la lampur!', 'terback!']
                number = random.randint(0, len(quoi_answer) - 1)
                answer = quoi_answer[number]
            else:
                answer = 'feur!'
            await message.channel.send(answer)
        #    if str(message.author) == 'Suyl/O#8304':
        #        await message.channel.send('csc')


def setup(bot):
    bot.add_cog(QuoiFeur(bot))
    print('QuoiFeur is loaded')
