# Даны три переменные: X, Y, Z. Их значения числа.
# Из данных произвольных чисел выбрать наибольшее.

# Пример:
# X = 5
# Y = 10
# Z = 3
# Ответ: Наибольшее число 10.
#
# X = 10
# Y = 12
# Z = -7
# Ответ: Наибольшее число 12.

import random

x = random.randint(-10000, 10000)
y = random.randint(-10000, 10000)
z = random.randint(-10000, 10000)

result = max(x, y, z)
print(str(x) + " " + str(y) + " " + str(z))
print(result)

