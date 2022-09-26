import re


def is_rhythm(some_text):
    task_list = some_text.split()
    pattern = re.compile(r'[аяуюоэиыеё]')
    result = set([sum([1 for verb in el if re.findall(pattern, verb)]) for el in task_list])
    return 'Парам пам-пам' if len(result) == 1 else 'Пам парам'


print(is_rhythm('Пара-ра-рам рам-пам-папам па-ра-па-дам'))
