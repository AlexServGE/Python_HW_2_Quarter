from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import commands
from messages import Messages

with open('Token.txt', 'r', encoding='utf-8') as file:
    token = file.read()

bot = Bot(token)
updater = Updater(token)
dispatcher = updater.dispatcher
messages = Messages()

greetings_handler = CommandHandler('start', commands.start_greetings)
dispatcher.add_handler(greetings_handler)

user_messages_handler = MessageHandler(Filters.text, messages.user_message)
dispatcher.add_handler(user_messages_handler)

updater.start_polling()
