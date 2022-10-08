from decimal import Decimal


class Rationalfigure:

    def __init__(self, a):
        self.a = Decimal(a)

    def __add__(self, other):
        return Rationalfigure(self.a + other.a)

    def __mul__(self, other):
        return Rationalfigure(self.a * other.a)

    def __sub__(self, other):
        return Rationalfigure(self.a - other.a)

    def __str__(self):
        return f'{self.a}'


if __name__ == '__main__':
    f_1 = Rationalfigure('1.2')
    f_2 = Rationalfigure('2.2')
    f_3 = f_1 + f_2
    print(f_1)
    print(f_2)
    print(f_3)
