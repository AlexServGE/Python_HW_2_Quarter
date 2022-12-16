import random


def who_is_first():
    return 1 if random.randint(0, 1) == 0 else 0


def bot_intelligence(sweets):
    return sweets - sweets // 28 * 28


def game_logic_player_1(sweets):
    while True:
        sweets_player = int(input('Ход игрока. Введите количество конфет, которые возьмете себе: '))
        sweets -= sweets_player
        print(f'Игрок взял: {sweets_player}. Осталось конфет: {sweets}')
        if sweets <= 0:
            print('Последние конфеты взял игрок')
            break
        print('Ход бота')
        sweets_bot = 28
        sweets -= sweets_bot
        print(f'Бот взял: {sweets_bot}. Осталось конфет: {sweets}')
        if sweets <= 0:
            print('Последние конфеты взял бот')
            break
        print(100 * '-')


def game_logic_bot_0(sweets):
    trigger = 0
    while True:
        print('Ход бота')
        if trigger == 0:
            sweets_bot = bot_intelligence(sweets)
            trigger = 1
        else:
            sweets_bot = sweets_player
        sweets -= sweets_bot
        print(f'Бот взял: {sweets_bot}. Осталось конфет: {sweets}')
        if sweets <= 0:
            print('Последние конфеты взял бот')
            break
        sweets_player = int(input('Ход игрока. Введите количество конфет, которые возьмете себе: '))
        sweets -= sweets_player
        print(f'Игрок взял: {sweets_player}. Осталось конфет: {sweets}')
        if sweets <= 0:
            print('Последние конфеты взял игрок')
            break
        print(100 * '-')


def game(sweets):
    first_turn = who_is_first()
    game_logic_player_1(sweets) if first_turn else game_logic_bot_0(sweets)


game(2021)
