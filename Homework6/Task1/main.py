# Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности.
# Пример [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]


def only_unique_elements(some_list):
    task_set = set(some_list)
    result = list()
    for el in task_set:
        if some_list.count(el) == 1: result += [el]
    return sorted(result)


user_input_list = [int(el) for el in input('Введите последовательность чисел через пробел: ').split()]
print(user_input_list)

print(only_unique_elements(user_input_list))
