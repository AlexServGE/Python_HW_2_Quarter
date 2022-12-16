# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

task_input = input('Введите буквы: ')

previous_el = 0
result = ''
counter = 0

for el in task_input:
    if el != previous_el:
        result += str(counter) + str(previous_el)
        previous_el = el
        counter = 1
    else:
        counter += 1
    if el == task_input[-1]:
        result += str(counter) + str(previous_el)

print(result[2:])
