import discord
from discord import app_commands
from discord.ext import commands
import random


class Roll(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with
        """
        self.bot = bot
        
    @app_commands.command(
        name="roll",
        description="Roll dices")
    @app_commands.describe(
        dice="The dice to roll",
        number="The number of dices to roll")
    async def roll(self, interaction: discord.Interaction, *, number: int, dice: int) -> None:
        """
        Roll dices and returns the result
        :param interaction: The interaction to respond to.
        :param dice: The dice to roll
        :param number: The number of dices to roll
        """
        if number > 100:
            await interaction.response.send_message('You can\'t roll more than 100 dice at once!')
            return
        if dice > 100:
            await interaction.response.send_message('You can\'t roll more than 100 sides on a dice!')
            return
        if number < 1:
            await interaction.response.send_message('You can\'t roll less than 1 dice!')
            return
        if dice < 1:
            await interaction.response.send_message('You can\'t roll less than 1 side on a dice!')
            return
        total = 0
        dice_number = []
        for i in range(number):
            dice_roll = random.randint(1, dice)
            dice_number.append(dice_roll)
        for i in dice_number:
            total += i

        embed = discord.Embed(title='Dices roll', description='You just roll **{0}** with **{1}** sides each'.format(
            number, dice), color=discord.Colour.blue())
        embed.set_author(name=interaction.user.name, icon_url=interaction.user.display_avatar.url)
        embed.add_field(name='Detailed number', value=dice_number, inline=False)
        embed.add_field(name='Total', value=total, inline=False)

        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(
        Roll(bot),
        guilds=[discord.Object(id=980975086154682378)]
    )
