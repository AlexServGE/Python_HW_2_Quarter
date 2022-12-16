# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$
# и выведите на экран их сумму.
import random


def sum_of_sequence(user_input):
    sequence = list()
    for el in range(1, user_input + 1):
        sequence.append(((1 + 1 / el) ** el))
    print(sequence)
    return sum(sequence)


sum_of_seq = lambda x: sum([((1 + 1 / el) ** el) for el in range(1, x + 1)])  # improved with lambda
print(sum_of_seq(10))


# 5. Реализуйте алгоритм перемешивания списка.


def mixer(user_input_list):
    random.shuffle(user_input_list)
    return user_input_list


task_list = [1, 'super', 2.0]
print(set(task_list))  # improved with set


# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_of_even_indexes(some_list):
    return sum(some_list[1::2])


user_input_list = [2, 3, 5, 9, 3, 6]
print(sum_of_even_indexes(user_input_list))
print(sum([el for idx, el in filter(lambda x: user_input_list.index(x[1], x[0]) % 2 != 0, enumerate(user_input_list))]))
# improved with filter, list comprehension, enumerate


# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import math


def mul_digits_pairs(some_list):
    return [some_list[i] * some_list[-i - 1] for i in range(math.ceil(len(some_list) / 2))] #improved with list comprehension


task_list_1 = [2, 3, 4, 5, 6]
print(mul_digits_pairs(task_list_1))
task_list_2 = [2, 3, 5, 6]
print(mul_digits_pairs(task_list_2))
