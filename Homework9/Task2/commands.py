

def start_greetings(update, context):
    context.bot.send_message(update.effective_chat.id, 'Добро пожаловать в бот, который калькулирует')
    context.bot.send_message(update.effective_chat.id, 'комплексные и вещественные числа. Выберите нужную Вам операцию:')
    context.bot.send_message(update.effective_chat.id, '1. Работа с комплексными числами')
    context.bot.send_message(update.effective_chat.id, '2. Работа с вещественными числами')
