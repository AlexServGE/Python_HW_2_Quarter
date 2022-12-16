# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import math


def mul_digits_pairs(some_list):
    return [some_list[i] * some_list[-i - 1] for i in range(math.ceil(len(some_list) / 2))]


task_list_1 = [2, 3, 4, 5, 6]
print(mul_digits_pairs(task_list_1))
task_list_2 = [2, 3, 5, 6]
print(mul_digits_pairs(task_list_2))
