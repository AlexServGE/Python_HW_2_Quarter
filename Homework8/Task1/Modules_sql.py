import sqlite3
from sqlite3 import Error
from Viewer import Viewer


class SQL:

    def __init__(self):
        self.viewer_sql = Viewer()
        self.con = self.sql_connection()
        self.table_name = None
        self.columns_tuple = None

    def sql_connection(self):
        try:
            con = sqlite3.connect('Company_internal.db')
            return con
        except Error:
            print(Error)

    def create_sql_table(self):
        cursor = self.con.cursor()
        self.table_name = self.viewer_sql.get_table_name()
        self.columns_tuple = self.viewer_sql.get_titles_new_table()
        command = f'CREATE TABLE if not exists {self.table_name}'
        flag = 0
        for el in self.columns_tuple:
            if flag == 0:
                command += f'({el} PRIMARY KEY,'
                flag = 1
            else:
                command += f'{el},'
        command = command[:-1] + ')'
        print(command)
        cursor.execute(command)
        self.con.commit()

    def add_employee(self):
        cursor = self.con.cursor()
        command = f'INSERT INTO {self.table_name} VALUES('
        for el in self.columns_tuple:
            if 'integer' in el:
                user_data = input(f'Введите {el} сотрудника: ')
                command += f"{user_data},"
            elif 'text' in el:
                user_data = input(f'Введите {el} сотрудника: ')
                command += f"'{user_data}',"
            elif 'real' in el:
                user_data = input(f'Введите {el} сотрудника: ')
                command += f"{user_data},"
        command = command[:-1] + ')'
        cursor.execute(command)
        self.con.commit()


if __name__ == '__main__':
    pass
