#
#  Определите класс Person. В конструктор которого передается фамилия и возраст ('Иванов', 29)
#  Реализуйте через магические методы условие, при котором возраст у объекта не будет меняться после инициализации.

class Person:
    second_name = ""
    __age = None

    def __init__(self, second_name, age):
        self.second_name = second_name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if self.__age is None:
            self.__age = age
        else:
            print("Beep")


a = Person("Иванов", 15)

print("Name:" + str(a.second_name) + " Age:" + str(a.age))

a.age = 23

print("Name:" + str(a.second_name) + " Age:" + str(a.age))
