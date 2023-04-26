#
# Поля:
# скорость;
# себестоимость перевозки груза;
# стоимость перевозки груза.
# В классе должны быть абстрактные методы:
# метод Cost (без параметров) – вычисление стоимости перевозки груза.
# Метод Info - информация (без параметров), который возвращает строку, содержащую информацию об объекте.
#
# На его основе реализовать дочерние классы:
# Marine - морской транспорт,
# Ground - наземный транспорт.

from abc import abstractmethod, ABC


class Transport(ABC):
    speed = 0
    cost_price = 0
    price = 0

    @abstractmethod
    def Cost(self):
        pass

    @abstractmethod
    def Info(self):
        pass


class Marine(Transport):
    name = "Marine transport"
    cost_price = 12

    def Info(self):
        print(self.name + " cost:" + str(self.cost_price) + " price: " + str(self.price))

    def Cost(self):
        self.price = self.cost_price * 5


class Ground(Transport):
    name = "Ground transport"
    cost_price = 12

    def Info(self):
        print(self.name + " cost:" + str(self.cost_price) + " price: " + str(self.price))

    def Cost(self):
        self.price = self.cost_price * 3


a = Ground()
a.Info()
a.Cost()
a.Info()

a = Marine()
a.Info()
a.Cost()
a.Info()
