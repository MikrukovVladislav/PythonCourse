#
#  Напишите функцию, которая принимает два аргумента, lst - список чисел и x – число.
#  Функция возвращает список, содержащий квадраты чисел из lst, которые больше числа x.
#  Сделайте несколько вариантов решений:
#  1) Просто цикл с условием.
#  2) Воспользуйтесь функцией filter, для чего создайте функцию проверки числа больше x
import random

lst = list()
for i in range(10):
    lst.append(random.randrange(0, 10000))

x = int(input("Введите х: "))


def func1(arr):
    global x
    result = list()
    for i in arr:
        if i > x:
            result.append(i ** 0.5)
    return result


def func2(arr):

    result = list(filter(lambda var: var > x, arr))
    for i in range(len(result)):
        result[i] **= 0.5
    return result

print(lst)

print(func1(lst))
print(func2(lst))
