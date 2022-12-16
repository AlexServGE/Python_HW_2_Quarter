# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import decimal

task_list_1 = [1.1, 1.2, 3.1, 5, 10.01]

sorted_float_list = lambda some_list: sorted(
    [float(decimal.Decimal(f'{el}') - int(el)) for el in some_list if type(el) is float])

task_result_list = lambda some_list: some_list[-1] - some_list[0]

print(task_result_list(sorted_float_list(task_list_1)))
