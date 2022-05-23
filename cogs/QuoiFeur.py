from discord.ext import commands
import re
import random


class QuoiFeur(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener(name='on_message')
    async def on_message(self, message):
        out = ((re.sub(r'[^\w\s]', '', message.content)).rstrip())
        end_quoi = out[len(out) - 4:len(out)]
        if end_quoi == "quoi" or end_quoi == "Quoi":
            if random.randint(0, 100) < 25:
                quoi_answer = ['chi!', 'drilatère!', 'ffage!', 'feuse!', 'ffure!', 'ffer!', 'driceps!', 'tuor!', 'druplé!', 'artz!', 'druple!', 'la lampur!', 'terback!']
                number = random.randint(0, len(quoi_answer) - 1)
                answer = quoi_answer[number]
            else:
                answer = 'feur!'
            await message.channel.send(answer)


def setup(bot):
    bot.add_cog(QuoiFeur(bot))
    print('QuoiFeur is loaded')
