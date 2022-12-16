from abv_purger import ABVpurger
import my_logging


class Messages:

    def __init__(self):
        self.abv_purger_messages = ABVpurger()

    def user_message(self, update, context):
        text = update.message.text
        my_logging.logging(update, context)
        reply = self.abv_purger_messages.abv_purge(text)
        context.bot.send_message(update.effective_chat.id, reply)
        reply = 'Введите текст или сообщение, в котором требуется удалить слова с указанной комбинацией символов.'
        context.bot.send_message(update.effective_chat.id, reply)
