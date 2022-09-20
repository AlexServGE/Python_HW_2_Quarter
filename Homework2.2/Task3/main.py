# 3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$
# и выведите на экран их сумму.


def sum_of_sequence(user_input):
    sequence = list()
    for el in range(1,user_input+1):
        sequence.append(((1 + 1 / el) ** el))
    print(sequence)
    return sum(sequence)


print(sum_of_sequence(2))