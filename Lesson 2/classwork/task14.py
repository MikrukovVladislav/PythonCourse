#Введите список lst, состоящий из чисел. Найдите и напечатайте наименьшее число из списка lst.
# B Python есть функция min, которая решает эту задачу. Но напишите свою функцию, которая не использует функцию min.
import random

cnt = int(input("Введите количество чисел: "))

if cnt > 0:
    lst = list()

    for i in range(cnt):
        lst.append(random.randint(0, 10000))

    min = lst[0]

    for i in range(len(lst)):
        if min > lst[i]:
            min = lst[i]

    print(lst)
    print("Min = " + str(min))

else:
    print("Incorrect value...")