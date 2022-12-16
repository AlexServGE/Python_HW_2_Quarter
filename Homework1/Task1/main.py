# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
#
# Пример:
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def is_weekend(n):
    print('Указано неправильное значение дня недели' if n < 1 or n > 7 else "нет" if 1 <= n <= 5 else "да")


is_weekend(6)
is_weekend(7)
is_weekend(1)
is_weekend(0)
is_weekend(8)