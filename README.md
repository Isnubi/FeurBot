<a name="readme-top"></a>

<!-- Projet Shields -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Isnubi/FeurBot/">
    <img src="docs/FeurBot.png" alt="Visualization">
  </a>


<h3 align="center">FeurBot</h3>
  <p align="center">
    <a href="https://github.com/Isnubi/FeurBot/"><strong>Explore the docs »</strong></a>
    <br />--------------------
    <br />
    <a href="https://github.com/Isnubi/FeurBot/issues">Report Bug</a>
    ·
    <a href="https://github.com/Isnubi/FeurBot/issues">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<div align="center">
    <img src="docs/FeurBot_Discord.png" alt="Logo">
</div>

FeurBot is a Discord bot, developed in Python, that can be used to play music, to do quizzes, to moderate a server, to display hardware statistics, and more.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![JSON][JSON]][JSON-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
<a name="getting-started"></a>

You can install FeurBot on your own server by following these steps.

### Prerequisites

1. Clone the repository on your computer.

    ```sh
    git clone https://github.com/Isnubi/FeurBot.git
    cd FeurBot
    ```

2. Install Python 3.8.5 or higher and pip. You can download it [here](https://www.python.org/downloads/) or by using the following command on Linux:

   * Debian/Ubuntu:
     ```sh
     sudo apt install python3 python3-pip -y
     ```
  
   * Fedora/CentOS/RHEL:
     ```sh
     sudo dnf install python3 python3-pip -y
     ```

3. Install the required python packages using pip:

    ```sh
    python3 -m pip install --upgrade pip
    python3 -m pip install requirements.txt
    ```
   If the requirements.txt file didn't work, you can install the required packages manually using the following command:
    ```sh
    python3 -m pip install discord.py psutil asyncio youtube_dl discord.py[voice] aiohttp
    ```


### Installation

1. Get a free Giphy API Key at [https://developers.giphy.com/](https://developers.giphy.com/)
2. Create a Discord bot and get its token at [https://discord.com/developers/applications](https://discord.com/developers/applications)
3. Enter your bot token and your Giphy API Key in `private/config.py`
    ```python
    giphy_api_key = "YOUR_GIPHY_TOKEN"
    token = "YOUR_DISCORD_TOKEN"
    ```
4. Run the bot
    ```sh
   python3 main.py
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Once the bot is launching, you can invite it to your server by using the invitation link you can create in your Discord Developer Portal.
<img src="docs/FeurBot_URL_Generator.png" alt="URL Generator">

* The default prefix of the bot is `!`. You can change it by sending the following command in a text channel: 
    ```
    !setprefix <prefix>
    ```
* You can get the current prefix by **mentioning** the bot.<br>
    <br><img src="docs/FeurBot_Prefix.png" alt="Prefix"><br><br>
* You can get the help menu by sending.
    ```
    !help
    ```
  You can navigate in it with the reactions.

_For more examples, please refer to the help menu of the bot._

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Gif system
- [ ] Music system
    - [x] Music player
    - [x] Music commands
    - [ ] Music queue

See the [open issues](https://github.com/Isnubi/FeurBot/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.md` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact


Isnubi - [@Louis_Gambart](https://twitter.com/Louis_Gambart) - contact@louis-gambart.fr
<br>**Discord:** isnubi#6221

**Project Link:** [https://github.com/Isnubi/FeurBot](https://github.com/Isnubi/FeurBot)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Isnubi/FeurBot.svg?style=for-the-badge
[contributors-url]: https://github.com/Isnubi/FeurBot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Isnubi/FeurBot.svg?style=for-the-badge
[forks-url]: https://github.com/Isnubi/FeurBot/network/members
[stars-shield]: https://img.shields.io/github/stars/Isnubi/FeurBot.svg?style=for-the-badge
[stars-url]: https://github.com/Isnubi/FeurBot/stargazers
[issues-shield]: https://img.shields.io/github/issues/Isnubi/FeurBot.svg?style=for-the-badge
[issues-url]: https://github.com/Isnubi/FeurBot/issues
[license-shield]: https://img.shields.io/github/license/Isnubi/FeurBot.svg?style=for-the-badge
[license-url]: https://github.com/Isnubi/FeurBot/blob/master/LICENSE.md
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/louis-gambart
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[JSON]: https://img.shields.io/badge/JSON-5E5C5C?style=for-the-badge&logo=json&logoColor=white
[JSON-url]: https://www.json.org/json-en.html
[Twitter-shield]: https://img.shields.io/twitter/follow/Louis_Gambart?style=social
[Twitter-url]: https://twitter.com/Louis_Gambart/