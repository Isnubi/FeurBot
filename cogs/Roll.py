import discord
from discord.ext import commands
import random


class Roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='roll')
    async def roll(self, ctx, *, args):
        try:
            rolls, limit = args.split('d')
        except ValueError:
            await ctx.send('Format has to be in [number]d[number]!')
            return
        try:
            rolls = int(rolls)
            limit = int(limit)
        except ValueError:
            await ctx.send('Format has to be in [number]d[number]!')
            return
        if rolls > 100:
            await ctx.send('You can\'t roll more than 100 dice at once!')
            return
        if limit > 100:
            await ctx.send('You can\'t roll more than 100 sides on a dice!')
            return
        if rolls < 1:
            await ctx.send('You can\'t roll less than 1 dice!')
            return
        if limit < 1:
            await ctx.send('You can\'t roll less than 1 side on a dice!')
            return
        total = 0
        dice_rolls = []
        for i in range(rolls):
            dice_roll = random.randint(1, limit)
            dice_rolls.append(dice_roll)
        for i in dice_rolls:
            total += i

        embed = discord.Embed(title='Dices roll', description='You just roll **{0}** with **{1}** sides each'.format(rolls, limit), color=discord.Colour.blue())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name='Detailed rolls', value=dice_rolls, inline=False)
        embed.add_field(name='Total', value=total, inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Roll(bot))
    print('Roll is loaded')
