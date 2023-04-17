# Напишите программу, которая получает на вход строку, и определяет,
# является ли строка панграммой (т.е. содержатся ли в ней все 33 буквы русского алфавита).

alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def pangramma(str):
    i = 0

    for i in range(len(alphabet)):
        if alphabet[i] in str:
            continue
        else:
            return False

    return True


tmpStr = "АБВГ ЕЁЖЗИЙК ЛМН ОПРСТУФХЦ ЧШЩЪЫЬЭЮЯД"

print(pangramma(tmpStr))