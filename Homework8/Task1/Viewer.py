class Viewer:

    def show_tables_menu(self):
        print("Выберите необходимое действие")
        print("1. Создать новую таблицу")
        print("2. Работать с имеющейся таблицей [в разработке Выбрать таблицу]")
        print("3. Закончить работу")
        print('-' * 100)
        user_choice = input("Введите номер необходимого действия: ")
        return user_choice

    def show_menu(self):
        print('-' * 100)
        print("Выберите необходимое действие")
        print("1. Добавить нового сотрудника")
        print("2. Перейти в предыдущее меню")
        print("3. Закончить работу")
        print('-' * 100)
        user_choice = input("Введите номер необходимого действия: ")
        return user_choice

    def get_table_name(self):
        return input('Введите название таблицы: ')

    def get_titles_new_table(self):
        return ("id integer", "last_name text", "first_name text", "position text", "phone_number integer",
                         "salary real")

    def get_employee(self):
        pass


if __name__ == '__main__':
    pass
