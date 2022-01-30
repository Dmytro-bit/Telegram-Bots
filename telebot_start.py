from email import message
import telebot
from telebot import types
token="2141034624:AAEIpDbb3N5cz4QEVp7XKZ4TpnWtWfvmFio"
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(messege):
    bot.send_message(messege.chat.id,"Hello")

@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item=types.KeyboardButton("Button")
    markup.add(item)
    bot.send_message(message.chat.id,"Wot you want",reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Button":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item=types.KeyboardButton("Button2")
        markup.add(item)
        bot.send_message(message.chat.id,"www.google.com",reply_markup=markup)
    elif message.text=="Button2":
        bot.send_message(message.chat.id,'Thanks for reading the site')

bot.infinity_polling()