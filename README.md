# Chriswallet_bot
Source code for Telegram @chriswallet_bot. Based on kotomei_bot

# Getting started
## Requirements
```
python 3.6 ^
pip
git
```
## Installing
To run this bot, you will need to instal [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) first.
```
$ pip install python-telegram-bot
```
Or you can install from source codes.
```
$ git clone https://github.com/python-telegram-bot/python-telegram-bot --recursive
$ cd python-telegram-bot
$ python setup.py install
```

Clone the codes of the bot.
```
git clone https://github.com/dz-paji/Chriswallet_bot
```
## Configuration 
Please fill in the token field in config.py which is the token of your telegram bot. To check or reset the token, please ask [@BotFather](https:t.me/BotFather)

To run this bot, you just need to enter the following command.
```
$ python main.py
```
If you did all the things above corrently, your bot should run successfully with absolutely no problem whatsoever.

To prevent program display logs , please change the bool value of `full_log` in `config.py` to `False`
To disable debug mode, please comment line 86 in `main.py`


