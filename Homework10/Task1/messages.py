from game_logic import Game


class Messages:

    def __init__(self):
        self.game = False
        self.score_bot = 0
        self.score_player = 0

    def user_message(self, update, context):
        text = update.message.text
        if self.game is False:
            if text.isdigit():
                self.game = Game(int(text))
                context.bot.send_message(update.effective_chat.id,
                                         f'Ход {update.effective_user.first_name}. Введите количество конфет, которые возьмете себе: ')
            else:
                context.bot.send_message(update.effective_chat.id, f'Ошибка! Требуется число!')
        else:
            self.game.game_logic(update, context)
            if self.game.bot_score == 1:
                self.score_bot += 1
                self.game = False
                context.bot.send_message(update.effective_chat.id, 'Введите общее количество конфет для начала игры:')
            elif self.game.player_score == 1:
                self.score_player += 1
                self.game = False
                context.bot.send_message(update.effective_chat.id, 'Введите общее количество конфет для начала игры:')
