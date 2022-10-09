from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from messages import Messages
from commands import Commands

with open('Token.txt', 'r', encoding='utf-8') as file:
    token = file.read()

bot = Bot(token)
updater = Updater(token)
dispatcher = updater.dispatcher
commands = Commands()
messages = Messages()

greetings_handler = CommandHandler('start', commands.start_greetings)
dispatcher.add_handler(greetings_handler)

user_messages_handler = MessageHandler(Filters.text, messages.user_message)
dispatcher.add_handler(user_messages_handler)

updater.start_polling()
