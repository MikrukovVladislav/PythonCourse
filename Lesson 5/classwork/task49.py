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
        print(self.__dict__)
        if "_Person__age" in self.__dict__:
            print("Beep")

        else:
            self.__age = age


a = Person("Иванов", 15)

print("Name:" + str(a.second_name) + " Age:" + str(a.age))

a.age = 23

print("Name:" + str(a.second_name) + " Age:" + str(a.age))
