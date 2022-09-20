# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fib_sequence(user_input):
    if user_input == 0:
        return [0]
    fib_list = [0, 1]
    for i in range(1, user_input):
        result = fib_list[i - 1] + fib_list[i]
        fib_list.append(result)
    left_fib_list = list()
    trigger = 1
    for el in fib_list:
        trigger *= -1
        left_fib_list.append(el*trigger)
    return left_fib_list[:1:-1] + fib_list


print(fib_sequence(8))
