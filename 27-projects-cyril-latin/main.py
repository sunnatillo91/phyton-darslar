# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 22:45:14 2022

Dasturlash asoslari

27-dars "KIRIL-LOTIN" telegram bot
"""

from transliterate import to_cyrillic, to_latin
import telebot
    
TOKEN = '5225536596:AAEPS_KPyXPIjZ-GClB6MBLAC8tycnmydbA'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob="Assalamu alaykum. Xush kelibsiz!" 
    javob+="\nMatn kiriting: "
    bot.reply_to(message, javob)
    
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msg = message.text
    # javob = lambda msg: to_cyrillic(msg) if msg.isascii() else: to_latin(msg)
    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)
    bot.reply_to(message, javob)    

bot.polling()
