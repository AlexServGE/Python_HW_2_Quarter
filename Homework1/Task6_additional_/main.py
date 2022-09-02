# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ...,
# где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#
# Требуется найти N-е число Фибоначчи.
#
# Входные данные
# Во входном файле INPUT.TXT записано целое число N (0 ≤ N ≤ 30).
#
# Выходные данные
# В выходной файл OUTPUT.TXT выведите N-е число Фибоначчи

# 0 1 1 2 3 5

def fibonacci(N):
    if N == 0:
        return 0
    elif N == 2 or N == 1:
        return 1
    else:
        return fibonacci(N - 1) + fibonacci(N - 2)


with open("INPUT.txt", 'r', encoding="utf-8") as i:
    number = int(i.read())

with open("OUTPUT.txt", 'w', encoding="utf-8") as o:
    o.write(str(fibonacci(number)))
