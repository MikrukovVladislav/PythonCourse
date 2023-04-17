#  Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().
# При решении задачи обратите внимание какой тип вы получаете через функцию input().

a = int(input("Print A: "))
b = int(input("Print B: "))
c = int(input("Print C: "))

print('A = ' + str(a) + ' B = ' + str(b) + ' C = ' + str(c))
print("AC = " + str(a - c) if a > c else str(c - a))
print("BC = " + str(b - c) if b > c else str(c - b))