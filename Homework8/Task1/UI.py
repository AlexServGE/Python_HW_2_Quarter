from Modules_sql import SQL
from Viewer import Viewer


class UI:

    def __init__(self):
        self.viewer_ui = Viewer()
        self.sql_1 = SQL()
        self.session_tables_organiser()

    def session_tables_organiser(self):
        while self.sql_1.table_name is None:
            user_choice = self.viewer_ui.show_tables_menu()
            if user_choice == '1':  # "1. Создать новую таблицу"
                self.sql_1.create_sql_table()
                user_choice = '2'
            if user_choice == '2' and self.sql_1.table_name is not None:  # "2. Работать с имеющейся таблицей [в разработке Выбрать таблицу]"
                self.session_table_editor()
            if user_choice == '2' and self.sql_1.table_name is None:
                print('\n!Вам требуется создать новую таблицу, что в ней работать!\n')
            if user_choice == '3':  # "3. Закончить работу"
                self.sql_1.con.close()
                break


    def session_table_editor(self):
        user_choice = self.viewer_ui.show_menu()
        while user_choice != '2' and user_choice != '3':
            if user_choice == '1':  # "1. Добавить нового сотрудника"
                self.sql_1.add_employee()
                user_choice = self.viewer_ui.show_menu()
        if user_choice == '2':  # "2. Перейти в предыдущее меню"
            self.sql_1.table_name = None                #!!!Криво
            self.session_tables_organiser()

        if user_choice == '3':  # "3. Закончить работу"
            self.sql_1.con.close()
