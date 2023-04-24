# Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.
import datetime
import time

log = {}


def dec_timer_func(func):
    def wrapper(*args, **kwargs):
        global log
        nonlocal a
        a += 1
        res = func(*args, **kwargs)
        log[func.__name__] = str(
            func.__name__ + ", " + str(a) + ", " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        return res

    a = 0
    return wrapper


@dec_timer_func
def test_func():
    time.sleep(0.1)
    return ""


@dec_timer_func
def test_func1():
    time.sleep(0.1)
    return ""


test_func()
test_func()
test_func()
test_func()
test_func()

test_func1()

with open("debug.log", "w") as f:
    for i in log.items():
        print(i)
        f.write(i[1] + '\n')
