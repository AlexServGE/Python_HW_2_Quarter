from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from messages import Messages

with open('Token.txt', 'r', encoding='utf-8') as file:
    token = file.read()

bot = Bot(token)
updater = Updater(token)
dispatcher = updater.dispatcher
messages = Messages()


def start_greetings(update, context):
    context.bot.send_message(update.effective_chat.id, 'Добро пожаловать в игру про конфеты.\n '
                                                       'Список доступных коман:\n'
                                                       '/start - начать новую игру \n'
                                                       '/score - посмотреть общий счет \n'
                                                       '/show_menu - показать меню команд\n'
                                                       'Кто последний возьмет конфеты, тот и победил.\n'
                                                       '(за раз можно взять не более 28 конфет)')
    context.bot.send_message(update.effective_chat.id, 'Введите общее количество конфет для начала игры:')


def show_menu(update, context):
    context.bot.send_message(update.effective_chat.id, 'Список доступных команд:\n'
                                                       '/start - начать новую игру \n'
                                                       '/score - посмотреть общий счет \n')


def show_score(update, context):
    context.bot.send_message(update.effective_chat.id, f'Счет на текущий момент:\n'
                                                       f'Бот: {messages.score_bot} \n'
                                                       f'Игрок: {messages.score_player}')  # ????


greetings_handler = CommandHandler('start', start_greetings)
dispatcher.add_handler(greetings_handler)

score_handler = CommandHandler('score', show_score)
dispatcher.add_handler(score_handler)

score_handler = CommandHandler('show_menu', show_menu)
dispatcher.add_handler(score_handler)

user_messages_handler = MessageHandler(Filters.text, messages.user_message)
dispatcher.add_handler(user_messages_handler)

updater.start_polling()
