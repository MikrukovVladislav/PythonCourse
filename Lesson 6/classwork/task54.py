#
#  Функция get_weekday()
#  Реализуйте функцию get_weekday(), которая принимает один аргумент:
#
#  number — целое число (от 1 до 7 включительно)
#  Функция должна возвращать полное название дня недели на русском, который соответствует числу number, при этом:
#
#  если number не является целым числом, функция должна возбуждать исключение:
#  TypeError('Аргумент не является целым числом')
#  если number является целым числом, но не принадлежит отрезку [1;7]
#  функция должна возбуждать исключение:
#  ValueError('Аргумент не принадлежит требуемому диапазону')
import numbers


#
# Сделайте функцию get_weekday() статической в классе Helper

class Helper():
    @staticmethod
    def get_weekday(num):
        names = ["Понедельник", "Вторник", "Среда",
                 "Четверг", "Пятница", "Суббота", "Воскресенье"]
        try:
            try:
                num = int(num)
            except ValueError:
                raise TypeError
            if (num > 0) and (num < 8):
                print(names[num - 1])
            else:
                raise ValueError

        except ValueError as e:
            print("Аргумент не принадлежит требуемому диапазону")
        except TypeError as e:
            print("Аргумент не является целым числом")


val = input("Введите номер дня недели: ")

Helper.get_weekday(val)
