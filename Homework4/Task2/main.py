# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.


def list_simple_muls(user_input):
    result = list()
    for i in range(2, 10):
        while user_input % i == 0:
            user_input = user_input // i
            result.append(i)
            if user_input == 1:
                return result
    if result:
        return result
    else:
        return 'Заданное число не является составным.'


print(list_simple_muls(600))
print(list_simple_muls(991))
print(list_simple_muls(97))
print(list_simple_muls(1))
