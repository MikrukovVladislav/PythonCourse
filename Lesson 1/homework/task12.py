# # Написать игру "Поле чудес"
#
# Отгадываемые слова и описание лежат в разных  массивах по одинаковому индексу.
# words = ["оператор", "конструкция", "объект"]
# desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования", "..", ".." ]
# Пользователю выводится определение слова и количество букв в виде шаблона. Стиль шаблона может быть любым.
# Слово из массива берется случайным порядком. Принимая из ввода букву мы ее открываем
# в случае успеха а в случае неуспеха насчитывам штрафные балы. Игра продолжается до 10 штрафных баллов
# либо победы.
#
# Пример вывода:
#
# "Это слово обозначает наименьшую автономную часть языка программирования"
#
# ▒  ▒  ▒  ▒  ▒  ▒  ▒  ▒
#
# Введите букву: O
#
# O  ▒  ▒  ▒  ▒  ▒  O  ▒
#
#
# Введите букву: Я
#
# Нет такой буквы.
# У вас осталось 9 попыток !
# Введите букву:
import random


def print_word(word, arr):
    result = ""
    for i in range(len(word)):
        if arr[i] == 1:
            result += word[i]
        else:
            result += "▒"

    return result

def check_win(arr):
    tmpVariable = 0
    for i in range(len(arr)):
        if(arr[i] == 1):
            tmpVariable+=1

    if tmpVariable == len(arr):
        return 1
    else:
        return 0

words = ["тест", "сет", "мед"]
desc = ["тест_деск", "сет-деск", "мед-деск"]

num_word = random.randrange(0, 3)

print(desc[num_word])

result_list = list()

for i in range(len(words[num_word])):
    result_list.append(0)

counter_errs = 0

while counter_errs < 10:
    print(print_word(words[num_word],result_list))

    ch = str(input("Введите символ: "))

    start = words[num_word].find(ch)
    if start != -1:
        while start != -1:
            result_list[start] = 1
            start = words[num_word].find(ch, start+1)
            print(start)
    else:
        counter_errs += 1
        print("Нет такой буквы! У вас осталось " + str(10 - counter_errs) + " попыток!")

    if(check_win(result_list) == 1):
        print("Вы победили")
        exit(1)