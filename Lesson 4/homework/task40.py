# Создайте функцию, которая принимает два аргумента, год и месяц, и возвращает list comprehension,
# содержащий все даты этого месяца в этом году. Используйте функцию monthrange(year, month) из модуля
# calendar для нахождения числа дней в месяце.
import calendar


def func(year, month):
    lst = [str(n) + "." + str(month) + "." + str(year) for n in range(1, calendar.monthrange(year, month)[1] + 1)]
    print(lst)

yr,mn = input("Введите через пробел год и месяц: ").split()

func(int(yr), int(mn))
