import re


class Contact:

    def __init__(self):

        self.surname = ['Фамилия', input('Введите фамилию нового контакта (Иванов):')]
        self.name = ['Имя', input('Введите имя нового контакта (Иван):')]
        self.father_name = ['Отчество', input('Введите отчество нового контакта (Иванович):')]
        self.phone = ['Телефон', input('Введите телефон нового контакта (+71112223344):')]
        self.work_place = ['Место работы', input('Введите место работы нового контакта (любой текст):')]
        contact_list = [self.surname, self.name, self.father_name, self.phone, self.work_place]
        self.is_contact_correct(contact_list)
        self.contact_list = '\t\t\t\t'.join([el[1] for el in contact_list])

    def is_contact_correct(self, contact_list):
        pattern_surname = re.compile(r'[А-ЯЁ][а-яё]+')
        pattern_name = re.compile(r'[А-ЯЁ][а-яё]+')
        pattern_father_name = re.compile(r'[А-ЯЁ][а-яё]+')
        pattern_phone = re.compile(r'\+\d{11}')
        # pattern_work_place = re.compile(r'?????')
        pattern_list = (pattern_surname, pattern_name, pattern_father_name, pattern_phone)
        for pattern, contact_detail, idx in zip(pattern_list, contact_list, range(len(contact_list))):
            while not contact_detail[1] or contact_detail[1] != ''.join(pattern.findall(contact_detail[1])):
                contact_detail[1] = input(f'Некорректный формат данных. Введите {contact_list[idx][0]}:')


class Writer:

    def __init__(self):
        self.contact_1 = Contact()
        self.contact_save(self.contact_1.contact_list)

    def contact_save(self, contact_list):
        with open(r'Phone_book.txt', 'a', encoding='utf-8') as phone_book:
            phone_book.write(f'{contact_list}\n')
