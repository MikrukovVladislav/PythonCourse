#
#     Напишите программу, которая определяет и печатает «похожие» слова. Слово называется похожим на другое слово,
#     если его гласные буквы находятся там же, где находятся гласные буквы другого слова, например:
#     дорога и пароход - похожие слова (гласные буквы на втором, четвертом и шестом местах),
#     станок и прыжок - похожие слова, питон и удав непохожие слова.
#     Считаем, что в русском языке 10 гласных букв (а, у, о, ы, и, э, я, ю, ё, е).
#     Ввод: x –первое слово, например, питон. n – количество слов для сравнения, например 6.
#     Дальше вводятся 6 слов, например: поросенок, титан, итог, лавка, погост, кино.
#     Вывод - слова, похожие на питон: титан, погост, кино

char_arr = ("а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е")

#x = str(input("Введите первое слово: "))
x = "питон"

#n = int(input("Введите количество слов для сравнения: "))
n = 6

#arr = str(input("Введите " + str(n) + " слов: ")).split(", ")
arr = ["поросенок", "титан", "итог", "лавка", "погост", "кино"]

template_arr = list(map(lambda var: set(map(lambda value: value[0] if value[1] in char_arr else False, list(enumerate(var)))), arr))
template_word = set(map(lambda value: value[0] if value[1] in char_arr else False, list(enumerate(x))))

template_word.discard(False)
for i in range(len(template_arr)):
    template_arr[i].discard(False)

result = []
for i in range(len(template_arr)):
    if template_arr[i] == template_word:
        result.append(arr[i])

print(result)