# Даны переменные A, B, C. Изменить их значения, переместив содержимое A в B, B — в C, C — в A,
# и вывести новые значения переменных A, B, C.

a = int(input("Input A: "))
b = int(input("Input B: "))
c = int(input("Input C: "))

a += b
b = a - b
a = a - b
a += c
c = a - c
a -= c

print("A = " + str(a) + " B = " + str(b) + "C = " + str(c))