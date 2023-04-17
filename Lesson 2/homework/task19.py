# Напишите калькулятор (простой). На вход подается строка, например:
# 1 + 2  или  5 – 3  или  3 * 4  или  10 / 2.
# Вывод: сосчитать и напечатать результат операции.
# Гарантируется, что два операнда и операция есть в каждой строчке, и все они разделены пробелами.

var = str(input("Введите выражение: "))

var_split = var.split(" ")

match var_split[1]:
    case '+':
        print(var + " = " + str(int(var_split[0]) + int(var_split[2])))
    case '-':
        print(var + " = " + str(int(var_split[0]) - int(var_split[2])))
    case '*':
        print(var + " = " + str(int(var_split[0]) * int(var_split[2])))
    case '/':
        print(var + " = " + str(int(var_split[0]) / int(var_split[2])))