# Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11

import string


def sum_digits_in_nums(user_input):
    nums = str(user_input)
    result = 0
    check_list = string.digits[1:]
    for el in check_list:
        result += int(el) * nums.count(el)
    return result


def test():
    assert sum_digits_in_nums(6782) == 23
    assert sum_digits_in_nums(0.56) == 11
    print('Программа работает корректно')


test()
print(sum_digits_in_nums(6782))
print(sum_digits_in_nums(0.56))
print(sum_digits_in_nums(1.25))
