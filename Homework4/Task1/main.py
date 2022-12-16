# Пользователь вводит число, Вам необходимо вывести число
# Пи с той точностью знаков после запятой,
# сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)

def pi_resque():
    result = 0
    for k in range(10):
        result += (1 / 16 ** k) * ((4 / (8 * k + 1)) - (2 / (8 * k + 4)) - (1 / (8 * k + 5)) - (1 / (8 * k + 6)))
    return result


def pi_length(pi, user_input):
    return '{0:.{1}f}'.format(pi, user_input)


task_user_input = int(input('''Введите число, получите число pi с введенным количеством знаков после запятой
(ограничение до 49 знаков): '''))
print(pi_length(pi_resque(), task_user_input))
