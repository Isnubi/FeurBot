#!/bin/sh
# This script is used to install the package and its dependencies


# Update system

echo "Updating system"
sudo apt-get update -y && sudo apt-get upgrade -y
echo "System updated"
echo "================================"
echo "================================"
echo "================================"


# Install the necessary packages for the bot

LIST="git python3 python3-pip mariadb-server mariadb-client"

for i in $LIST; do
    echo "Installing $i"
    sudo apt install "$i" -y
    echo "$i installed"
    echo "================================"
done
echo "Packages installed"
echo "================================"
echo "================================"
echo "================================"


# Install the python dependencies

echo "Installing python dependencies"
python3 -m pip install -r requirements.txt
echo "Python dependencies installed"
echo "================================"
echo "================================"
echo "================================"


# Create the database

echo "Creating the database"
mysql -u root -p < FeurBot.sql
echo "Database created"
echo "================================"
echo "================================"
echo "================================"


echo "Installation complete"
echo "You now need to edit the private/config.py file to add your bot token and database credentials"
echo "You can run, after that, the bot with the command: python3 FeurBot.py"
echo "================================"