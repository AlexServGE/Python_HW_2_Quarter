# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math


def distance2D(x1, y1, x2, y2):
    result = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return round(result, 2)


print(distance2D(3, 6, 2, 1))
print(distance2D(7, -5, 1, -1))
