from Writer import Writer
from Reader import Reader
from Viewer import Viewer


class UI:

    def __init__(self):
        print('Вас приветствует приложение: Справочник\n')
        self.viewer = Viewer()
        self.session_start()

    def session_start(self):
        while self.viewer.show_menu() != '3':
            if self.viewer.menu == '1':
                user_choice = self.viewer.show_write_menu()
                for i in range(user_choice):
                    Writer()
            elif self.viewer.menu == '2':
                search_surname = self.viewer.show_contact_by_surname()
                Reader().get_contact_surname(search_surname)
