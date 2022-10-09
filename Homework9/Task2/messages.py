from math_complex_nums import Complexfigure
from math_rational_nums import Rationalfigure
from user_inputs_parser import Parser
from decimal import Decimal
import my_logging


class Messages:

    def __init__(self):
        self.complex_messages = ComplexMessages()
        self.rational_messages = RationalMessages()

    def user_message(self, update, context):
        text = update.message.text
        my_logging.logging(update, context)
        if self.complex_messages.trigger is False and self.rational_messages.trigger is False:
            self.welcome_first_figure(update, context, text)
        elif self.complex_messages.trigger is True:
            self.complex_messages.complex_user_messages(update, context, text)
        elif self.rational_messages.trigger is True:
            self.rational_messages.rational_user_messages(update, context, text)

    def welcome_first_figure(self, update, context, text):
        if '1' in text:
            reply = 'Введите комплексное число (например: 1+2i):'
            context.bot.send_message(update.effective_chat.id, reply)
            self.complex_messages.trigger = True
        if '2' in text:
            reply = 'Введите вещественное число (например: 1.2):'
            context.bot.send_message(update.effective_chat.id, reply)
            self.rational_messages.trigger = True


class ComplexMessages:
    trigger = False
    figure_1, action, figure_2, step = 0, None, 0, 0

    def complex_user_messages(self, update, context, text):
        if self.step == 0:
            a, b = Parser().complex_figure_parser(text)
            self.figure_1 = Complexfigure(int(a), int(b))
            self.welcome_second_figure(update, context)
            self.step = 1
        elif self.step == 1:
            a, b = Parser().complex_figure_parser(text)
            self.figure_2 = Complexfigure(int(a), int(b))
            self.welcome_action(update, context)
            self.step = 2
        elif self.step == 2:
            self.action = text
            result = self.result_calculation(self.figure_1, self.action, self.figure_2)
            context.bot.send_message(update.effective_chat.id, f'Ответ: {result}')
            self.trigger = False
            self.figure_1, self.action, self.figure_2, self.step = 0, None, 0, 0
            context.bot.send_message(update.effective_chat.id, f'Выберите нужную Вам операцию: ')
            context.bot.send_message(update.effective_chat.id, '1. Работа с комплексными числами')
            context.bot.send_message(update.effective_chat.id, '2. Работа с вещественными числами')

    def result_calculation(self, a, action, b):
        if action == '+':
            return a + b
        elif action == '-':
            return a - b
        elif action == '*':
            return a * b

    def welcome_action(self, update, context):
        reply = 'Выберите операцию для введенных чисел:'
        context.bot.send_message(update.effective_chat.id, reply)
        reply = 'Сложение: +\n' \
                'Вычитание: -\n' \
                'Умножение: *\n'
        context.bot.send_message(update.effective_chat.id, reply)

    def welcome_second_figure(self, update, context):
        reply = 'Введите второе комплексное число (например: 1-2i):'
        context.bot.send_message(update.effective_chat.id, reply)


class RationalMessages:
    trigger = False
    figure_1, action, figure_2, step = 0, None, 0, 0

    def rational_user_messages(self, update, context, text):
        if self.step == 0:
            self.figure_1 = Rationalfigure(Decimal(text))
            self.welcome_second_figure(update, context)
            self.step = 1
        elif self.step == 1:
            self.figure_2 = Rationalfigure(Decimal(text))
            self.welcome_action(update, context)
            self.step = 2
        elif self.step == 2:
            self.action = text
            result = self.result_calculation(self.figure_1, self.action, self.figure_2)
            context.bot.send_message(update.effective_chat.id, f'Ответ: {result}')
            self.trigger = False
            self.figure_1, self.action, self.figure_2, self.step = 0, None, 0, 0
            context.bot.send_message(update.effective_chat.id, f'Выберите нужную Вам операцию: ')
            context.bot.send_message(update.effective_chat.id, '1. Работа с комплексными числами')
            context.bot.send_message(update.effective_chat.id, '2. Работа с вещественными числами')

    def result_calculation(self, a, action, b):
        if action == '+':
            return a + b
        elif action == '-':
            return a - b
        elif action == '*':
            return a * b

    def welcome_action(self, update, context):
        reply = 'Выберите операцию для введенных чисел:'
        context.bot.send_message(update.effective_chat.id, reply)
        reply = 'Сложение: +\n' \
                'Вычитание: -\n' \
                'Умножение: *\n'
        context.bot.send_message(update.effective_chat.id, reply)

    def welcome_second_figure(self, update, context):
        reply = 'Введите второе вещественное число (например: 1.2):'
        context.bot.send_message(update.effective_chat.id, reply)
