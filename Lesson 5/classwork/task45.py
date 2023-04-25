#
#  Создайте класс Triangle с методом, который при создании объекта проверяет три переменный x, y, z на то,
#  что из них можно составить треугольник. Требования: все числа должны быть больше нуля, сумма любых двух должны быть больше третьего.


class Triangle:
    x = 0
    y = 0
    z = 0

    def __init__(self, x, y, z):
        if x > 0 and y > 0 and z > 0:
            if x < y + z or y < x + z or z < x + y:
                self.x = x
                self.y = y
                self.z = z
            else:
                print("сумма любых двух должны быть больше третьего")
        else:
            print("все числа должны быть больше нуля")


a = Triangle(0, 1, 2)
b = Triangle(1, 1, 1)

print(a.x)
print(b.x)
