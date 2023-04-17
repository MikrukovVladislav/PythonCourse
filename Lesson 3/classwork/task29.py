#   todo:
#  Реализуйте функцию convert(), которая принимает один аргумент:
#  number — целое число
#  Функция должна возвращать кортеж из трех элементов, расположенных в следующем порядке:
#  двоичное представление числа number в виде строки без префикса 0b
#  восьмеричное представление числа number в виде строки без префикса 0o
#  шестнадцатеричное представление числа number в виде строки в верхнем регистре без префикса 0x
#  Примечание 1. В задаче удобно воспользоваться функциями bin(), oct() и hex().
#  Задачу решить доступным способом
#  Задачу решить с помощью применения функции map и lambda

def func1(var):
    result = (str(bin(var))[2:], str(oct(var))[2:], str(hex(var)).upper()[2:])
    return result


def func2(var):
    tmp_result = (bin, str(oct(var)), str(hex(var)).upper())
    result = tuple(map(lambda  fn: fn()[2:], tmp_result))

    return result


number = 256

print(func1(number))
print(func2(number))
