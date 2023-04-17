# Дано множество, состоящее из чисел. Его можно ввести одной строкой с пробелами между числами
#  с помощью оператора tes=set(map(int, input().split())).
#  Напечатайте среднее арифметическое введенных чисел. Воспользуйтесь функциями sum и len.

import random

tes = set()

cnt = int(input("Введите количество чисел: "))

for i in range(cnt):
    tes.add(random.randint(0, 10000))

print(tes)
print("Сумма = " + str(sum(tes)))
print("Среднее арифметическое = " + str(sum(tes) / len(tes)))