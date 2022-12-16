class ABVpurger:
    text = None

    def abv_purge(self, text: str):
        return ' '.join(list(filter(lambda x: 'абв' not in x, text.split())))

    def __str__(self):
        return self.text


if __name__ == '__main__':
    task_text = 'Сегодняабв дождлиабввый день, но скоро выйдет солнце'
    result_text = ABVpurger().abv_purge(task_text)
    print(result_text)
