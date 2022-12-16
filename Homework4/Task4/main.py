# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random


def coefficients_list(user_input):
    result = [random.randint(0, 100) for el in range(user_input + 1)]
    return result


def equation(coefficients):
    result = ''
    for idx, el in enumerate(coefficients):
        if el > 1:
            if len(coefficients) - 1 == idx:
                result += '{0}'.format(el)
            elif len(coefficients) - 2 == idx:
                result += '{0}*x+'.format(el)
            else:
                result += '{0}*x^{1}+'.format(el, len(coefficients) - idx - 1)
        elif el == 1:
            if len(coefficients) - 1 == idx:
                result += '{0}'.format(el)
            elif len(coefficients) - 2 == idx:
                result += 'x+'
            else:
                result += 'x^{0}+'.format(len(coefficients) - idx - 1)
        else:
            if len(coefficients) - 1 == idx:
                result = result[:-1]
                break
            else:
                continue
    return result


print(equation(coefficients_list(5)))
print(equation([6,0,0,2,0]))
print(equation([6,0,0,0,2]))
print(equation([6,0,0,0,1]))
print(equation([6,0,0,1,1]))
print(equation([1,1,1,1]))
