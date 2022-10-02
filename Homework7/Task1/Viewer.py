class Viewer:

    def __init__(self):
        self.menu = None

    def show_menu(self):
        menu = input('Выберите действие:\n '
                     '1. Внести новый контакт \n '
                     '2. Найти и вывести контакт по фамилии\n '
                     '3. Завершить работу\n'
                     'Укажите свой выбор [1/2/3]: ')
        self.menu = menu
        return menu

    def show_write_menu(self):
        user_choice = int(input('Сколько контактов требуется внести [1/2/..]: '))
        return user_choice

    def show_contact_by_surname(self):
        user_choice = input('Введите фамилию искомого контакта: ')
        return user_choice
