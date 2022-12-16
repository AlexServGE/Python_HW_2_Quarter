import re


class Player:

    def __init__(self):
        self.name = input('Введите свой никнейм: ')
        self.identity = input(f'{self.name}, введите крестик или нолик для определения Вашего знака в игре: ')
        self.count = 0

    def turn(self):
        decision_coordinates = input(f'[{self.name}], введите координаты для постановки[формат ввода:№№]: ')
        return decision_coordinates

    def is_in_desk_borders(self, decision_coordinates):
        i, j = decision_coordinates
        if int(i) > 2 or int(j) > 2:
            return False
        elif int(i) < 0 or int(j) < 0:
            return False
        else:
            return True


class Desk:
    def __init__(self):
        self.desk = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

    def __str__(self):
        for el in self.desk:
            print(el)
        return ''


class Game:
    def __init__(self):
        self.player_1 = Player()
        self.player_2 = Player()
        self.plate = Desk()
        self.x_0_game()
        print(self.who_is_winner())

    def who_is_winner(self):
        sign_1 = self.player_1.identity
        sign_2 = self.player_2.identity
        for el in self.plate.desk:
            counter_1 = el.count(sign_1)
            counter_2 = el.count(sign_2)
            if counter_1 == 3:
                self.player_1.count += 1
            elif counter_2 == 3:
                self.player_2.count += 1
        counter_q_1 = 0
        counter_z_1 = 0
        counter_q_2 = 0
        counter_z_2 = 0
        desk_side = len(self.plate.desk)
        for i, j in enumerate(range(desk_side)):
            if self.plate.desk[i][j] == sign_1:
                counter_q_1 += 1
            elif self.plate.desk[i][j] == sign_2:
                counter_q_2 += 1
            if self.plate.desk[desk_side - 1 - i][desk_side - 1 - j] == sign_1:
                counter_z_1 += 1
            elif self.plate.desk[desk_side - 1 - i][desk_side - 1 - j] == sign_1:
                counter_z_2 += 1
        if counter_q_1 == 3:
            self.player_1.count += 1
        elif counter_q_2 == 3:
            self.player_2.count += 1
        if counter_z_1 == 3:
            self.player_1.count += 1
        elif counter_z_2 == 3:
            self.player_2.count += 1
        if self.player_1.count > self.player_2.count:
            return f'Победитель: {self.player_1.name}'
        elif self.player_1.count < self.player_2.count:
            return f'Победитель: {self.player_2.name}'
        else:
            return f'НИЧЬЯ'

    def cell_is_not_filled(self, decision_coordinates):
        i, j = list(decision_coordinates)
        return True if self.plate.desk[int(i)][int(j)] == '.' else False

    def plate_has_free_cells(self):
        pattern = re.compile(r'\.')
        text = pattern.findall(str(self.plate.desk))
        return True if text else False

    def x_0_game(self):
        while True:
            print(self.plate)
            decision_coordinates = self.player_1.turn()
            if self.player_1.is_in_desk_borders(decision_coordinates):
                if self.cell_is_not_filled(decision_coordinates):
                    i, j = list(decision_coordinates)
                    self.plate.desk[int(i)][int(j)] = self.player_1.identity
                    if not self.plate_has_free_cells():
                        print(self.plate)
                        break
                else:
                    print(f'К сожалению, эта ячейка уже занята. Ход передается {self.player_2.name}')
            else:
                print(f'К сожалению, вы выбрали ячейку за пределами игрового поля. Ход передается {self.player_2.name}')
            print(self.plate)
            decision_coordinates = self.player_2.turn()
            if self.player_2.is_in_desk_borders(decision_coordinates):
                if self.cell_is_not_filled(decision_coordinates):
                    i, j = list(decision_coordinates)
                    self.plate.desk[int(i)][int(j)] = self.player_2.identity
                    if not self.plate_has_free_cells():
                        print(self.plate)
                        break
                else:
                    print(f'К сожалению, эта ячейка уже занята. Ход передается {self.player_1.name}')
            else:
                print(f'К сожалению, вы выбрали ячейку за пределами игрового поля. Ход передается {self.player_1.name}')


game = Game()
