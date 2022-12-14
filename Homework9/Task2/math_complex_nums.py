class Complexfigure:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complexfigure(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complexfigure(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)

    def __sub__(self, other):
        return Complexfigure(self.a - other.a, self.b - other.b)

    def __str__(self):
        if self.a != 0:
            if self.b > 0:
                return f'{self.a}+{self.b}i'
            elif self.b == 0:
                return f'{self.a}'
            else:
                return f'{self.a}{self.b}i'
        else:
            if self.b == 0:
                return f'0'
            else:
                return f'{self.b}i'


if __name__ == '__main__':
    f_1 = Complexfigure(0, 1)
    f_2 = Complexfigure(2, 0)
    f_3 = f_1 + f_2
    print(f_1)
    print(f_2)
    print(f_3)
    f_4 = f_1 * f_2
    print(f_4)
