import discord
from discord import app_commands
from discord.ext import commands
import re
import random


class QuoiFeur(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with
        """
        self.bot = bot

    @commands.Cog.listener(name='on_message')
    async def on_message(self, message):
        """
        Listens for messages and responds accordingly
        If message end with 'quoi' or 'Quoi', it will respond with a random quote from the list
        It except punctuation and special characters at the end of the message
        It is a French joke
        :param message: The message to listen to
        """
        out = ((re.sub(r'[^\w\s]', '', message.content)).rstrip())
        end_quoi = out[len(out) - 4:len(out)]
        end_qwa = out[len(out) - 3:len(out)]
        if end_quoi == "quoi" or end_quoi == "Quoi":
            if random.randint(0, 100) < 25:
                quoi_answer = ['chi!', 'drilatère!', 'ffage!', 'feuse!', 'ffure!', 'ffer!', 'driceps!', 'tuor!', 'druplé!', 'artz!', 'druple!', 'la lampur!', 'terback!']
                number = random.randint(0, len(quoi_answer) - 1)
                answer = quoi_answer[number]
            else:
                answer = 'feur!'
            await message.reply(answer)
        if end_qwa == "qwa" or end_qwa == "Qwa":
            await message.reply('ckQwack')

        await self.bot.process_commands(message)


async def setup(bot: commands.Bot):
    await bot.add_cog(
        QuoiFeur(bot),
        guilds=[discord.Object(id=980975086154682378)]
    )
