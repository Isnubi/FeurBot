from discord.ext import commands
import discord
import random
import json
import asyncio


class QuizSystem(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with
        """
        self.bot = bot

    @commands.command(name='quiz', aliases=['q'])
    async def quiz(self, ctx):
        """
        Send a random quiz question
        :param ctx: The context of the command
        """
        with open('private/quiz.json', 'r') as f:
            quiz = json.load(f)

        answers = []
        emoji1 = '1\u20E3'
        emoji2 = '2\u20E3'
        emoji3 = '3\u20E3'
        emoji4 = '4\u20E3'

        random_key = random.choice(list(quiz.keys()))
        question = quiz[random_key]['question']['question']
        realanswer = quiz[random_key]['real answer']['answer1']
        answers.append(realanswer)
        for i in range(2, 5):
            key = 'answer' + str(i)
            answers.append(quiz[random_key]['fake answer'][key])
        random.shuffle(answers)

        embed = discord.Embed(title=f'{quiz[random_key]["category"]}', description=question, color=discord.Color.blue())
        embed.add_field(name='First answer', value=f'{answers[0]}', inline=False)
        embed.add_field(name='Second answer', value=f'{answers[1]}', inline=False)
        embed.add_field(name='Third answer', value=f'{answers[2]}', inline=False)
        embed.add_field(name='Fourth answer', value=f'{answers[3]}', inline=False)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

        await ctx.message.delete()
        message = await ctx.send(embed=embed)
        await message.add_reaction(emoji1)
        await message.add_reaction(emoji2)
        await message.add_reaction(emoji3)
        await message.add_reaction(emoji4)

        def check(reaction, user):
            """
            Checks if the reaction is valid
            :param reaction: The reaction to check
            :param user: The user who reacted
            """
            return user == ctx.author and str(reaction.emoji) in [emoji1, emoji2, emoji3, emoji4]

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('Time is up!')
        else:
            user_answer = str(reaction.emoji)[0:-1]

            for i in range(len(answers)):
                if answers[i] == realanswer:
                    good_answer = i
                    break
            if user_answer == str(good_answer + 1):
                embed = discord.Embed(title='Correct answer!', description=f'{ctx.author.mention}', color=discord.Color.green())
                embed.set_author(name=f'{ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
            else:
                embed = discord.Embed(title='Wrong answer!', description=f'{ctx.author.mention}', color=discord.Color.red())
                embed.add_field(name='The correct answer was:', value=f'{realanswer}', inline=False)
                embed.set_author(name=f'{ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')

            await ctx.send(embed=embed)

    @commands.command(name='addquiz', aliases=['aq'])
    @commands.is_owner()
    async def addquiz(self, ctx, question, category, realanswer, answer2, answer3, answer4):
        """
        Add a new quiz question
        :param ctx: The context of the command
        :param question: The question
        :param category: The category of the question
        :param realanswer: The real answer
        :param answer2: One of the fake answers
        :param answer3: One of the fake answers
        :param answer4: One of the fake answers
        """
        with open('private/quiz.json', 'r') as f:
            quiz = json.load(f)

        q_object = {
            'question': {
                'question': question
            },
            'category': category,
            'real answer': {
                'answer1': realanswer
            },
            'fake answer': {
                'answer2': answer2,
                'answer3': answer3,
                'answer4': answer4
            }
        }

        quiz.update({len(quiz) + 1: q_object})

        with open('private/quiz.json', 'w') as f:
            json.dump(quiz, f, indent=4)

        embed = discord.Embed(title='Question added!', description=f'{ctx.author.mention}', color=discord.Color.blue())
        embed.set_author(name=f'{self.bot.user.name}', icon_url=f'{self.bot.user.avatar_url}')
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command(name='quizlist', aliases=['ql'])
    @commands.is_owner()
    async def quizlist(self, ctx):
        """
        Lists all the quiz questions
        :param ctx: The context of the command
        """
        with open('private/quiz.json', 'r') as f:
            quiz = json.load(f)

        questions = []
        for question in quiz:
            q_number = question
            q_question = quiz[question]['question']['question']
            questions.append((q_number, q_question))

        embed = discord.Embed(title='Quiz list', description=f'{ctx.author.mention}', color=discord.Color.blue())
        embed.set_author(name=f'{self.bot.user.name}', icon_url=f'{self.bot.user.avatar_url}')
        for i in range(0, len(quiz), 25):
            for quiz in questions[i:i + 25]:
                embed.add_field(name=f'Question {quiz[0]}', value=f'{quiz[1]}', inline=False)
            await ctx.send(embed=embed)
            embed.clear_fields()

        await ctx.message.delete()


    @commands.command(name='removequiz', aliases=['rq'])
    @commands.is_owner()
    async def removequiz(self, ctx, question_number):
        """
        Removes a quiz question
        :param ctx: The context of the command
        :param question_number: The question number
        """
        with open('private/quiz.json', 'r') as f:
            quiz = json.load(f)

        if question_number in quiz:
            del quiz[question_number]
            with open('private/quiz.json', 'w') as f:
                json.dump(quiz, f, indent=4)

            embed = discord.Embed(title='Question removed!', description=f'{ctx.author.mention}', color=discord.Color.blue())
            embed.set_author(name=f'{self.bot.user.name}', icon_url=f'{self.bot.user.avatar_url}')
        else:
            embed = discord.Embed(title='Question not found!', description=f'{ctx.author.mention}', color=discord.Color.red())
            embed.set_author(name=f'{self.bot.user.name}', icon_url=f'{self.bot.user.avatar_url}')
        await ctx.message.delete()
        await ctx.send(embed=embed)


def setup(bot):
    """
    Initializes the cog
    :param bot: bot object
    """
    bot.add_cog(QuizSystem(bot))
    print('QuizSystem is loaded')
