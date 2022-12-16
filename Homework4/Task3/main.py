# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.

def no_monkey_list(user_list):
    wip_list = sorted(user_list)
    i, result = 0, list()
    while i < len(wip_list):
        result += [wip_list[i]]
        counter = wip_list.count(wip_list[i]) - 1
        i += counter + 1
    return result


monkey_list_1 = [1, 2, 3, 4, 4, 3, 2, 5]
print(no_monkey_list(monkey_list_1))

monkey_list_2 = [1, 2, 3, 4, 4, 7, 7, 8, 8, 8, 8, 8, 3, 2, 5]
print(no_monkey_list(monkey_list_2))
