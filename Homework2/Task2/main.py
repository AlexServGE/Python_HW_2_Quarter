def sum_numbers(user_input):
    result = 0
    for el in range(user_input + 1):
        result += el
    return result

n = int(input("Введите N чисел: "))
print(sum_numbers(n))
