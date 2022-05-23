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
            await ctx.send('Format has to be in NdN!')
            return
        try:
            rolls = int(rolls)
            limit = int(limit)
        except ValueError:
            await ctx.send('Format has to be in NdN!')
            return
        if rolls > 100:
            await ctx.send('You can\'t roll more than 100 dice at once!')
            return
        if limit > 100:
            await ctx.send('You can\'t roll more than 100 sides on a dice!')
            return
        if rolls <= 0:
            await ctx.send('You can\'t roll less than 1 dice!')
            return
        if limit <= 0:
            await ctx.send('You can\'t roll less than 1 side on a dice!')
            return
        if rolls > 1:
            msg = 'Rolling {} dice with {} sides each...'.format(rolls, limit)
        else:
            msg = 'Rolling {} die with {} sides...'.format(rolls, limit)
        await ctx.send(msg)
        total = 0
        dice_rolls = []
        for i in range(rolls):
            dice_roll = random.randint(1, limit)
            dice_rolls.append(dice_roll)
        for i in dice_rolls:
            total += i
        await ctx.send('Total: {}'.format(total))
        await ctx.send('Rolls: {}'.format(dice_rolls))


def setup(bot):
    bot.add_cog(Roll(bot))
    print('Roll is loaded')
