import random


def random_generated_coins(N):
    return [random.randint(0, 1) for el in range(N)]


def count_coins_to_turn(coins):
    return coins.count(1)


coins_1 = random_generated_coins(10)
print(coins_1)
print(count_coins_to_turn(coins_1))
