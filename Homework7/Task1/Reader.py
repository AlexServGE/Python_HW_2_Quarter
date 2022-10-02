class Reader:

    def __init__(self):
        self.search_result_list: list = list()

    def get_contact_surname(self, search_surname):
        with open('Phone_book.txt', 'r', encoding='utf-8') as phone_book:
            content = phone_book.read().splitlines()
            for contact in content:
                result_list = list()
                if search_surname in contact:
                    print(contact)
                    result_list.append(contact)
        self.search_result_list = result_list


if __name__ == '__main__':
    search = Reader().get_contact_surname('Петров')
