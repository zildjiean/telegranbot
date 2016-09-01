#/usr/bin/python


import telebot
import os

bot = telebot.TeleBot("187648619:AAHmhxGQiTvu2snyCsrJ3S6LwEZQIpI8i5w")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "/checkweb : Check Website")

#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#    bot.reply_to(message, message.text)

@bot.message_handler(commands=['checkweb'])
def execute(message):
        command = str(message.text).split(" ")[1:]
        executeCommand(commands)

bot.polling()
