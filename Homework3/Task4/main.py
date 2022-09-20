# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def dec_to_bin(user_input):
    result = ""
    while user_input:
        if user_input % 2 > 0:
            result += "1"
        else:
            result += "0"
        user_input = user_input // 2
    return result[::-1]


task_user_input = int(input('Введите десятичное число:'))

print(bin(task_user_input)[2:])
print('{0:b}'.format(task_user_input))
print(dec_to_bin(task_user_input))
