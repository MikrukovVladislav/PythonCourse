# Задача 1 Переопределите метод __str__, чтобы в нем печатались
# все атрибуты объекта и их значения через запятую. Например:
# def __init__(self):
#     self.x = 0
#     self.y = 1
#
# Должно быть напечатано x:0, y:1

class test:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        var = ""
        for i in self.__dict__.items():
            if var != "":
                var += ", "
            var += str(i[0]) + ":" + str(i[1])
        return var


a = test(2, 3)

print(a)
