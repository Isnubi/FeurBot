# FeurBot

**FeurBot** is a Discord bot developed in *Python* which provides multiples command for users of discord server.

## Dependencies

FeurBot have been tested in a *3.7.3 Python environment*.

FeurBot use different libraries, such as [discord.py](https://github.com/Rapptz/discord.py) and [psutil](https://github.com/giampaolo/psutil).
These libraries can be installed using **pip3** command.

```bash
pip3 install discord.py
pip3 install psutil
```

## Usage

Once bot files have been forked and dependencies installed, you just have to run the **main.py** file.

```bash
python3 main.py
```

The bot will be launch and the cogs will be loaded.

![bot launching](docs/FeurBot_launch.png)

Once the bot is loaded, anytime a command is called by a user, a line will be printed in the console.

![bot command output](docs/FeurBot_command-output.png)

There is the list of all the commands available:

* **!help**: display the list of commands
* **!ping**: display the bot latency
* **!roll**: roll a dice
* **!say**: make the bot say something
* **!pfp**: display the user profile picture
* **!cpu**: display the CPU usage
* **!ram**: display the RAM usage
* **!temp**: display the CPU temperature
* **!purge**: delete a number of messages

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

You can also contact me on Discord (**isnubi#6221**) for any contributing or bug submission.

## Developer

This bot is completely developed by [Louis GAMBART](https://github.com/Isnubi).