#
#  Напишите рекурсивную функцию sumn(n), которая вычисляет и печатает сумму чисел от 0 до n.
import functools


def sumn(n):
    a = list(range(0, n + 1))
    result = functools.reduce(lambda x, y: x + y, a)
    return result


n = int(input("Введите число n: "))

print("Sumn = " + str(sumn(n)))
