# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

task_text = 'Сегодняабв дождлиабввый день, но скоро выйдет солнце'

result = filter(lambda x: 'абв' not in x, task_text.split())

print(*result)