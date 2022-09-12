import random


def random_array_with_berries(number_of_fields):
    return {el + 1: random.randint(0, 4) for el in range(number_of_fields)}


number_of_fields = int(input('Введите количество грядок: '))
if number_of_fields < 3:
    print('Ошибка! Начните программу заново. Программа работает с количеством грядок равным или более 3')
    exit(9)


user_random_array = random_array_with_berries(number_of_fields)
for idx, el in user_random_array.items():
    print(idx, el)

user_select_field = int(input('Введите номер грядки: '))

if user_select_field > number_of_fields:
    result_select_field = user_select_field % number_of_fields
else:
    result_select_field = user_select_field

if result_select_field == 1:
    print(user_random_array[number_of_fields] + user_random_array[result_select_field] + user_random_array[
        result_select_field + 1])
elif result_select_field == number_of_fields:
    print(user_random_array[result_select_field - 1] + user_random_array[result_select_field] +
          user_random_array[1])
else:
    print(user_random_array[result_select_field - 1] + user_random_array[result_select_field] +
          user_random_array[result_select_field + 1])

print('Очень торопился со сдачей. Прошу прощения за кривое написание кода без использования собственных функций')