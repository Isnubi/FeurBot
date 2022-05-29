import asyncio
import discord
import youtube_dl
from discord.ext import commands


# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''


# Setup YTDL options
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',
}

# FFmpeg options
ffmpeg_options = {'options': '-vn', }

# Setup YTDL
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        """
        Initializes the source with the given data and volume
        :param source: The source of the audio
        :param data: The data of the audio
        :param volume: The volume of the audio
        """
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        """
        Creates a source from a given url
        :param url: The url of the audio
        :param loop: The loop of the audio
        :param stream: Whether the audio is a stream or not
        """
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
    def __init__(self, bot):
        """
        Initializes the bot object
        :param bot: The bot to initialize the cog with
        """
        self.bot = bot

    @commands.command(name='join')
    async def join(self, ctx):
        """
        Let the bot join your voice channel
        :param ctx: The context of the command
        """
        try:
            channel = ctx.message.author.voice.channel
            if channel is None:
                embed = discord.Embed(title="FeurMusic", description='You are not in a voice channel', color=discord.Colour.blue())
                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            else:
                embed = discord.Embed(title="FeurMusic", description='Connecting to {0} voice channel'.format(ctx.message.author.voice.channel), color=discord.Colour.blue())
                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                await channel.connect()
        except discord.ClientException:
            embed = discord.Embed(title="FeurMusic", description='I\'m already used in another channel', color=discord.Colour.blue())
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        except AttributeError as e:
            embed = discord.Embed(title="FeurMusic", description='You are not in a voice channel', color=discord.Colour.blue())
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command(name='play')
    async def play(self, ctx, *, url):
        """
        Play a song from a given url
        :param ctx: The context of the command
        :param url: The url of the song
        """
        try:
            async with ctx.typing():
                player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
                ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)

            embed = discord.Embed(title="FeurMusic", url=url, description="Now playing: {0}".format(player.title), color=discord.Colour.blue())
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url=player.data['thumbnail'])

            await ctx.message.delete()
            await ctx.send(embed=embed)
        except youtube_dl.DownloadError as e:
            pass

    @commands.command(name='volume')
    async def volume(self, ctx, volume: int):
        """
        Change the volume of the player
        :param ctx: The context of the command
        :param volume: The volume to set the player to
        """
        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        embed = discord.Embed(title="FeurMusic", description='Volume set to {0}%'.format(volume), color=discord.Colour.blue())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command(name='pause')
    async def pause(self, ctx):
        """
        Pause the player
        :param ctx: The context of the command
        """
        ctx.voice_client.pause()
        embed = discord.Embed(title="FeurMusic", description='Music paused', color=discord.Colour.blue())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command(name='resume')
    async def resume(self, ctx):
        """
        Resume the player
        :param ctx: The context of the command
        """
        ctx.voice_client.resume()
        embed = discord.Embed(title="FeurMusic", description='Music resumed', color=discord.Colour.blue())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command(name='stop')
    async def stop(self, ctx):
        """
        Stop the player
        :param ctx: The context of the command
        """
        ctx.voice_client.stop()
        embed = discord.Embed(title="FeurMusic", description='Music stopped', color=discord.Colour.blue())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command(name='leave')
    async def leave(self, ctx):
        """
        Leave the voice channel
        :param ctx: The context of the command
        """
        await ctx.voice_client.disconnect()
        embed = discord.Embed(title="FeurMusic", description='Disconnected from voice channel', color=discord.Colour.blue())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

        await ctx.message.delete()
        await ctx.send(embed=embed)

    @play.before_invoke
    async def ensure_voice(self, ctx):
        """
        Ensure that the bot is connected to a voice channel
        :param ctx: The context of the command
        """
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()


def setup(bot):
    """
    Initializes the cog
    :param bot: bot object
    """
    bot.add_cog(Music(bot))
    print('PlaySound is loaded')
