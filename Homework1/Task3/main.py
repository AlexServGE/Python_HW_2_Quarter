# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


def stone_age_opencv(x,y):
    if x == 0 and y == 0:
        print('Заданы некорректные вводные данные')
    else:
        if x == 0 or y == 0:
            if x == 0 and y > 0:
                print('на оси Y "сверху"')
            elif x == 0 and y < 0:
                print('на оси Y "снизу"')
            elif x > 0 and y == 0:
                print('на оси X "справа"')
            else:
                print('на оси X "слева"')
        else:
            if x > 0 and y > 0:
                print(1)
            elif x > 0 and y < 0:
                print(4)
            elif x < 0 and y > 0:
                print(2)
            else:
                print(3)

stone_age_opencv(34,-30)
stone_age_opencv(2,4)
stone_age_opencv(-34,-30)
stone_age_opencv(0,-30)
stone_age_opencv(0,0)
