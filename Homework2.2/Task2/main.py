# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def mul_1_to_N(user_input):
    mulch = 1
    result = list()
    for i in range(1, user_input+1):
        mulch = mulch * i
        result.append(mulch)
    return result


print(mul_1_to_N(4))
