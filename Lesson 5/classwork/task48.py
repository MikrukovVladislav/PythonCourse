#
#  Создайте класс Shape, объекты которого имеют атрибуты
#  Colour – строка, например, «Красный», «Синий»;
#  Square – площадь объекта.
#  Создайте несколько методов:
#  1) Установить цвет объекта.
#  2) Запросить цвет объекта и напечатать его.
#  3) Задать площадь объекта.
#  4) Запросить площадь  объекта.

class Shape():
    Colour = ""
    Square = 0

    def set_colour(self, var):
        self.Colour = var

    def get_colour(self):
        print("Colour: " + str(self.Colour))

    def set_square(self, var):
        self.Square = var

    def get_square(self):
        return self.Square


a=Shape()

a.get_colour()
a.set_colour("red")
a.get_colour()

print("Square: " + str(a.get_square()))
a.set_square(123)
print("Square: " + str(a.get_square()))