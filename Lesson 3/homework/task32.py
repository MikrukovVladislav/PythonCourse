# Дан генетический код ДНК (строка, состоящая из букв G, C, T, A)
# Постройте РНК, используя принцип замены букв: G → C, C → G, T → A, A→T.
# Напишите функцию, которая на вход получает ДНК, и возвращает РНК. Например:
# Ввод: GGCTAA
# Вывод: CCGATT

tmp = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'T'}


def func(arr):
    result = ''.join(map(lambda x: tmp[x], arr))
    return str(result)


a = "GGCTAA"

print(func(a))
