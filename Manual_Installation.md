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
    <img src="docs/FEURBOT.png" alt="Visualization">
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


<!-- MANUAL INSTALLATION -->
## Manual Installation of the bot

If the install.sh script doesn't work for you, you can follow these steps to install the bot manually.

1. Install Python 3.8.5 or higher and pip. You can download it [here](https://www.python.org/downloads/) or by using the following command on Linux:

   * Debian/Ubuntu:
     ```sh
     sudo apt install python3 python3-pip -y
     ```
  
   * Fedora/CentOS/RHEL:
     ```sh
     sudo dnf install python3 python3-pip -y
     ```

2. Install the required python packages using pip:

    ```sh
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    ```
   
   If the requirements.txt file didn't work, you can install the required packages manually using the following command:
    ```sh
    python3 -m pip install discord.py psutil asyncio youtube_dl discord.py[voice] aiohttp mysql-connector-python
    ```

3. Install MariaDB or MySQL. You can download it [here](https://mariadb.org/download/) or by using the following command on Linux:

   * Debian/Ubuntu:
     ```sh
     sudo apt install mariadb-server mariadb-client -y
     ```
  
   * Fedora/CentOS/RHEL:
     ```sh
     sudo dnf install mariadb-server mariadb-client -y
     
4. Create a database for FeurBot. You can do it by using the following command on Linux:

    * Debian/Ubuntu:
      ```sh
      sudo mysql -u root -p
      ```
      
    * Fedora/CentOS/RHEL:
      ```sh
      sudo mysql -u root -p
      ```
      
    Then, you can create the database by using the following command:
      ```sh
      CREATE DATABASE FeurBot;
      CREATE USER 'FeurBot'@'localhost' IDENTIFIED BY 'FeurBot';
      GRANT ALL PRIVILEGES ON FeurBot.* TO 'FeurBot'@'localhost';
      FLUSH PRIVILEGES;
      ```
   
    You can now create the tables using the SQL script.
    ```sh
    mysql -u FeurBot -p FeurBot < FeurBot.sql
    ```

<br><br>**You can now following the next steps in the [README](README.md) file.**



<!-- CONTACT -->
## Contact


Isnubi - [@Louis_Gambart](https://twitter.com/Louis_Gambart) - [contact@louis-gambart.fr](mailto:contact@louis-gambart.fr)
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
[Mysql]: https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white
[Mysql-url]: https://www.mysql.com/
[Twitter-shield]: https://img.shields.io/twitter/follow/Louis_Gambart?style=social
[Twitter-url]: https://twitter.com/Louis_Gambart/