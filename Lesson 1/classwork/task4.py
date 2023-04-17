# Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0).
# Примечание: коэффициенты получаем через функцию input().

a = int(input("Print A: "))

while a < 0:
    a = int(input("Print A(Need A > 0): "))

b = int(input("Print B: "))

print("A*x + b = 0")
print("x = " + str(-b/a))