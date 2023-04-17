#
# Создайте лямбда функцию, которая принимает один параметр – строку.
# Переводит все буквы в нижний регистр и переворачивает их в обратном порядке. Пример входа: ‘ACbdzYx’,
# Вывод: 'xyzdbca'

test_str = "ACbdzYx"

test_str.lower()

test_lambda = lambda var : ''.join(reversed(str(var).lower()))

print(test_lambda(test_str))