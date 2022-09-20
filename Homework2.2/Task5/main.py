# 5. Реализуйте алгоритм перемешивания списка.

import random


def mixer(user_input_list):
    random.shuffle(user_input_list)
    return user_input_list


task_list = [1, 'super', 2.0]
print(mixer(task_list))
