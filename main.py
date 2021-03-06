#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import random
from telegram.ext import Updater, MessageHandler, BaseFilter, Filters

import config


class FilterGiveMoneySpecial(BaseFilter):
    def __init__(self):
        self.regex = re.compile(r'/(givememoney)+(@chriswallet(_bot)?)?( |$)')

    def filter(self, message):
        return bool(message.text and self.regex.search(message.text) is not None)


class FilterGiveMoney(BaseFilter):
    def __init__(self):
        self.regex = re.compile(r'/(givememoney)+(@.+)')

    def filter(self, message):
        return bool(message.text and self.regex.search(message.text) is not None)

class FilterDressing(BaseFilter):
    def __init__(self):
        self.regex = re.compile(r'/(dressing)+(@chriswallet(_bot)?)?( |$)')
    
    def filter(self, message):
        return bool(message.text and self.regex.search(message.text) is not None)

class FilterDressingOther(BaseFilter):
    def __init__(self):
        self.regex = re.compile(r'/(dressing)+(@.+)0')
    
    def filter(self, message):
        return bool(message.text and self.regex.search(message.text) is not None)


def givememoney_list(bot, update):
    text = ''
    name = update.message.from_user.username

    if name is not None and name.lower() in config.offer_money_list:
        text += '账单已提交，请老板查收 @' + update.message.from_user.username 
        update.message.reply_text(text)
    else: 
        if random.randint(1, 100) <= config.react_rate:
            text += random.choice(config.chris_qoute)
            update.message.reply_text(text)
        else:
            text += config.default_qoute
            update.message.reply_text(config.chris_qoute)
    

def givememoney(bot, update):
    update.message.reply_text(config.chris_qoute)


def dressing(bot, update):
    dressing_text = ''
    name = update.message.from_user.username

    if name is not None and name.lower() in config.dressing_special_list:
        update.message.reply_text('主人是不可以女装的！')
    elif name is not None and name.lower() not in config.dressing_special_list and random.randint(1, 100) <= config.dressing_react_rate: 
        dressing_text += '@' + update.message.from_user.username + ' 没经过任何反抗就被套上了女装'
        
    elif name is not None and name.lower() not in config.dressing_special_list and random.randint(1,100) >= config.dressing_react_rate:
        #TODO
        dressing_text += '@' + update.message.from_user.username + random.choice(config.dressing_process)
    elif name is None:
        dressing_text += '你需要有个用户名才能女装辣'

    update.message.reply_text(dressing_text)


def debug(bot, update):
    print(update.message.from_user.name + ' 发送了不存在的 ' + update.message.text + '')


def main():
    # logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    config.offer_money_list = [name.lower() for name in config.offer_money_list]
    config.dressing_special_list = [name.lower() for name in config.dressing_special_list]

    updater = Updater(config.token)

    updater.dispatcher.add_handler(MessageHandler(FilterGiveMoneySpecial(), givememoney_list))
    updater.dispatcher.add_handler(MessageHandler(FilterGiveMoney(), givememoney))
    updater.dispatcher.add_handler(MessageHandler(FilterDressing(), dressing))
    updater.dispatcher.add_handler(MessageHandler(Filters.all, debug)) # Debug 

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()
