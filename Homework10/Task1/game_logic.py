import random


class Game:

    def __init__(self, sweets):
        self.total_sweets = sweets
        self.bot_score = 0
        self.player_score = 0

    def game_logic(self, update, context):
        text = update.message.text
        if text.isdigit() and int(text) <= 28:
            self.total_sweets -= int(text)
            context.bot.send_message(update.effective_chat.id,
                                     f'{update.effective_user.first_name} взял {text}. Осталость {self.total_sweets} конфет.')
            if self.total_sweets > 0:
                bot_sweets = random.randint(1, 29)
                self.total_sweets -= bot_sweets
                context.bot.send_message(update.effective_chat.id,
                                         f'Бот взял {bot_sweets}. Осталость {self.total_sweets} конфет.')
                if self.total_sweets > 0:
                    context.bot.send_message(update.effective_chat.id,
                                             f'Ход {update.effective_user.first_name}. Введите количество конфет, которые возьмете себе: ')
                else:
                    context.bot.send_message(update.effective_chat.id,
                                             f'ПОБЕДИЛ БОТ. Осталость {self.total_sweets} конфет.')
                    self.bot_score += 1
            else:
                context.bot.send_message(update.effective_chat.id,
                                         f'ПОБЕДИЛ {update.effective_user.first_name}. Осталость {self.total_sweets} конфет.')
                self.player_score += 1
        else:
            context.bot.send_message(update.effective_chat.id, f'Ошибка! Требуется число меньше 28!')


if __name__ == '__main__':
    game = Game(2021)
