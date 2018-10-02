#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import random
from telegram.ext import Updater, MessageHandler, BaseFilter, Filters

import config


class FilterPr(BaseFilter):
    def __init__(self):
        self.regex = re.compile(r'/(givememoney)+(@chriswallet(_bot)?)?( |$)')

    def filter(self, message):
        return bool(message.text and self.regex.search(message.text) is not None)


class FilterPrOther(BaseFilter):
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


def pr(bot, update):
    text = ''

    name = update.message.from_user.username
    if name is not None and name.lower() in config.prpr_back:
        text += '我把钱都换成美金了，没钱给你了' + update.message.from_user.username 
            
    if config.full_log is True:
        print('在特殊关照名单中的 '+update.message.from_user.name + ' 发送了 givememoney 指令')


    update.message.reply_text(text)


def pr_other(bot, update):
    update.message.reply_text(config.other_emoticon)

    if config.full_log is True:
        print(update.message.from_user.name + '发送了 givememoney 指令')


def dressing(bot, update):
    dressing_text = ''
    dressing_text += '已经成功为 ' + update.message.from_user.username + ' 穿上女装'
    update.message.reply_text(dressing_text)
    if config.full_log is True:
        print(update.message.from_user.name + '发送了 dressing 指令')

def debug(bot, update):
    print(update.message.from_user.name + ' 发送了 ' + update.message.text + '已造成回调失败')


def main():
    # logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    config.prpr_back = [name.lower() for name in config.prpr_back]

    updater = Updater(config.token)

    updater.dispatcher.add_handler(MessageHandler(FilterPr(), pr))
    updater.dispatcher.add_handler(MessageHandler(FilterPrOther(), pr_other))
    updater.dispatcher.add_handler(MessageHandler(FilterDressing(), dressing))
    updater.dispatcher.add_handler(MessageHandler(Filters.all, debug))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()
