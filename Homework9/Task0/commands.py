class Commands:

    def start_greetings(self, update, context):
        context.bot.send_message(update.effective_chat.id, 'Добро пожаловать в бот, который удаляет из строки все слова, содержащие "абв". '
                                                           'Введите текст или сообщение, в котором требуется удалить слова с'
                                                           'указанной комбинацией символов.')


