# Напишите программу, в которой используется две функции.
# В одной программа «спит» 2 секунды, в другой – 3 секунды. Пусть каждая функция возвращает время, которое она «проспала».
# Главная программа запускает цикл от 0 до 10, если число четное, то запускает функцию с 2 секундами,
# если нечетное, то функцию с 3 секундами. Накапливает сон обеих функций отдельно и печатает две суммы.
import time


def sleep2():
    start_time = time.time()
    time.sleep(0.2)
    return time.time() - start_time


def sleep3():
    start_time = time.time()
    time.sleep(0.3)
    return time.time() - start_time


lst_a = []
lst_b = []

{lst_a.append(sleep2()) if i % 2 == 0 else lst_b.append(sleep3()) for i in range(0, 11)}

print(str(sum(lst_a)) + ":" + str(sum(lst_b)))




