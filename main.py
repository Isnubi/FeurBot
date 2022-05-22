from private.config import token # get token

# import libraries
import random
import re
import subprocess
import psutil
# import discord bot libraries
from discord.ext import commands
import discord


# set box prefix to "!"
bot = commands.Bot(command_prefix='!')


# alert in the console when bot is ready
@bot.event
async def on_ready():
    print('Bot ready!')


# command to check bot delay
@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}s of delay'.format(round(bot.latency, 1)))


# command to show Raspberry Pi temperature
@bot.command()
async def temp(ctx):
    temp_result = subprocess.run(['cat', '/home/isnubi/discordpy/temp'], stdout=subprocess.PIPE) # replace path to /sys/class/thermal/thermal_zone0/temp if you have sudo rights on the host
    temp_result = temp_result.stdout.decode('utf-8')
    temp_message = temp_result[0:2] + '.' + temp_result[3] + '°C'
    if int(temp_result[0:2]) < 45:
        temp_embed = discord.Embed(title="Température", description=temp_message, color=0x008000)
    elif int(temp_result[0:2]) >= 50:
        temp_embed = discord.Embed(title="Température", description=temp_message, color=0xff0000)
    else:
        temp_embed = discord.Embed(title="Température", description=temp_message, color=0xff7f00)
    await ctx.send(embed=temp_embed)


# command to get global CPU usage via psutil
@bot.command()
async def cpu(ctx):
    cpu_usage = psutil.cpu_percent(interval=0.5)
    cpu_message = str(cpu_usage) + '%'
    embed_cpu = discord.Embed(title="Usage du CPU", description=cpu_message, color=0x008000)
    await ctx.send(embed=embed_cpu)


# command to get global memory usage via psutil
@bot.command()
async def ram(ctx):
    ram_usage = psutil.virtual_memory().percent
    ram_message = str(ram_usage) + '%'
    embed_ram = discord.Embed(title="Usage de la RAM", description=ram_message, color=0x008000)
    await ctx.send(embed=embed_ram)


# command to purge channel with int arg in entry
@bot.command()
async def purge(ctx, purge_amount: int):
    await ctx.channel.purge(limit=purge_amount)


# event to answer a random word in a list when "quoi" end string (excepting ponctuation and space)
@bot.event
async def on_message(message):
    out = ((re.sub(r'[^\w\s]', '', message.content)).rstrip())
    end = out[len(out)-4:len(out)]
    if end == "quoi" or end == "Quoi":
        if random.randint(0,100) < 25:
            quoi_answer = ['chi!', 'drilatère!', 'ffage!', 'feuse!', 'ffure!', 'ffer!', 'driceps!', 'tuor!', 'druplé!', 'artz!', 'druple!', 'la lampur!', 'terback!']
            number = random.randint(0, len(quoi_answer) - 1)
            answer = quoi_answer[number]
        else:
            answer = 'feur!'
        await message.channel.send(answer)
#    if str(message.author) == 'Suyl/O#8304':
#        await message.channel.send('csc')
    await bot.process_commands(message)


bot.run(token)
