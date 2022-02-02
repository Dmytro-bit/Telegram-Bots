from telegram.ext import Updater
import logging
from telegram.ext import CallbackContext
from telegram import Update
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

updater = Updater(token='2141034624:AAEIpDbb3N5cz4QEVp7XKZ4TpnWtWfvmFio', use_context=True)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
dispatcher = updater.dispatcher



def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def caps(update: Update, context: CallbackContext):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

dispatcher.add_handler(echo_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
