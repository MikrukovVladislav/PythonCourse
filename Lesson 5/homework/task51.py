#
# Определите класс Person. При создании объекта p=Person(‘Иванов’, ‘Михаил’, ‘Федорович’) необходимо ввести полное имя человека.
# При печати объекта должно выводиться следующее:
# print(p) # чивородеФлиахиМвонавИ

class Person:
    first_name = ""
    second_name = ""
    third_name = ""

    def __init__(self, first_name, second_name, third_name):
        self.first_name = first_name
        self.second_name = second_name
        self.third_name = third_name

    def __str__(self):
        return (self.third_name[::-1]+self.second_name[::-1]+self.first_name[::-1])

p=Person("Иванов", "Михаил", "Федорович")

print(p)