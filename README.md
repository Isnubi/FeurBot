# FeurBot

**FeurBot** is a Discord bot developed in *Python* which provides multiples command for users of discord server.

## Dependencies

FeurBot have been tested in a *3.7.3 Python environment*.

FeurBot use different libraries, such as 
[discord.py](https://github.com/Rapptz/discord.py) 
and [psutil](https://github.com/giampaolo/psutil).
These libraries can be installed using **pip3** command.

```bash
pip3 install discord.py
pip3 install psutil
pip3 install asyncio
pip3 install youtube_dl
pip3 install discord.py[voice]
```

## Usage

Once bot files have been forked and dependencies installed, 
you just have to run the **main.py** file.

```bash
python3 main.py
```

The bot will be launch and the cogs will be loaded.

![bot launching](docs/FeurBot_launch.png)

Once the bot is loaded, anytime a command is called by a user, 
a line will be printed in the console.

![bot command output](docs/FeurBot_command-output.png)

The default prefix for the bot is **!**.

Mention the bot will answer you the current prefix used by the server.

### Commands list

There is the list of all the commands available:

General commands :
* **!help**: display the list of commands
* **!ping**: display the bot latency
* **!serverinfo**: display the server information
* **!userinfo**: display the user information

Fun commands :
* **!quiz**: display a random quiz

Level system commands :
* **!level**: display the current level of the user
* **leaderboard**: display the leaderboard

User commands :
* **!roll**: roll a dice
* **!say**: make the bot say something
* **!pfp**: display the user profile picture

Music commands :
* **!join**: let the bot join your voice channel
* **!play** : play a song (from YouTube URL)
* **!volume** : change the volume of the music
* **!pause** : pause the music
* **!resume** : resume the music
* **!stop** : stop the music
* **!leave** : let the bot leave your voice channel

Admin commands :
* **!purge**: delete a number of messages
* **!setprefix**: change the bot prefix
* **!kick**: kick a user
* **!ban**: ban a user
* **!unban**: unban a user
* **!banlist**: display the list of banned users

Hardware statistics commands :
* **!cpu**: display the CPU usage
* **!ram**: display the RAM usage
* **!temp**: display the CPU temperature

Bot owner commands :
* **!coglist**: display the list of cogs
* **!load**: load a cog
* **!unload**: unload a cog
* **!reload**: reload a cog
* **!reloadall**: reload all cogs
* **!addquiz**: add a question to the quiz
* **!removequiz**: remove a question from the quiz
* **!quizlist**: display the list of questions

## Contributing

Pull requests are welcome. For major changes, please open an issue 
first to discuss what you would like to change.

Please make sure to update tests as appropriate.

You can also contact me on Discord (**isnubi#6221**) for any contributing 
or bug submission.

## Developer

This bot is completely developed by 
[Louis GAMBART](https://github.com/Isnubi).

## License

[MIT](https://choosealicense.com/licenses/mit/)