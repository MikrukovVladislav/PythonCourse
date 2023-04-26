# Создать абстрактный класс Press (пресса) содержащий:
# Поля: название, цена за единицу.
# В классе должны быть абстрактные методы:
# метод SetPrice (без параметров) – установка цены.
# Метод Info - информация (без параметров), который возвращает строку, содержащую информацию об объекте.
#
# На его основе реализовать дочерние классы:
# Magazine - журнал,
# Book- книга.
import abc
from abc import ABC


class Press(ABC):
    name = ""
    price = 0

    @abc.abstractmethod
    def SetPrice(self):
        pass

    @abc.abstractmethod
    def Info(self):
        pass


class Book(Press):

    def __init__(self):
        self.name = "Книга"

    def SetPrice(self):
        self.price = 85

    def Info(self):
        print("Book name = " + str(self.name) + " Book price = " + str(self.price))


class Magazine(Press):

    def __init__(self):
        self.name = "Журнал"

    def SetPrice(self):
        self.price = 32

    def Info(self):
        print("Magazine name = " + str(self.name) + " Magazine price = " + str(self.price))


book = Book()
book.Info()
book.SetPrice()
book.Info()

magazine = Magazine()
magazine.Info()
magazine.SetPrice()
magazine.Info()
