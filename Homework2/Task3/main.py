def minimum_divider(n):
    if n % 2 == 0:
        for el in range(2, n - 1):
            if n % el == 0:
                return el
        return f'Минимального делителя числа {n} не существует.'
    else:
        for el in range(3, n - 1):
            if n % el == 0:
                return el
        return f'Минимального делителя числа {n} не существует.'


print(minimum_divider(15))
print(minimum_divider(35))
