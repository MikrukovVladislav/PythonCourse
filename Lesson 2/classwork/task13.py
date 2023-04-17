# Ввести число n. Напечатать треугольник из символов +.
#  Пример для n = 5:
# +
# ++
# +++
# ++++
# +++++

n = int(input("Введите число строк треугольника: "))

if(n > 0):
    string = ""
    while(n > 0):
        string += "+"
        print(string)
        n -= 1
else:
    print("Incorrect value...")
