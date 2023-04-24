#
#   Создайте класс Pet с атрибутам имя, вес и уровень сытости.
#   Напишите метод info, который в качестве результата выдает эти атрибуты.
#   Напишите метод hungry, который возвращает уровень сытости и комментирует: если меньше 5, то «голоден», если больше 10, то «сыт».
#   Напишите метод feed, который передает питомцу некоторую еду, которая прибавляется к уровню сытости и вызывает метод info.

class Pet():
    name = ""
    weight = 0
    hungry_lvl = 0

    def __init__(self, name, weight, hungry_lvl):
        self.name = name
        self.weight = weight
        self.hungry_lvl = hungry_lvl

    def info(self):
        print("name=" + str(self.name) + " weight=" + str(self.weight) + " hungry_lvl=" + str(self.hungry_lvl))

    def hungry(self):
        print("lvl: " + str(self.hungry_lvl) + " Голоден" if self.hungry_lvl < 5 else
              "lvl: " + str(self.hungry_lvl) + " Сыт" if self.hungry_lvl > 10 else "lvl: " + str(self.hungry_lvl))

    def feed(self, food):
        self.hungry_lvl += food
        self.info()


a = Pet("test", 10, 2)
a.info()
a.hungry()
a.feed(5)
a.feed(5)
