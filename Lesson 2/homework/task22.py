# Напишите функцию, которая шифрует строку, содержащую латинские буквы с помощью шифра Цезаря. Каждая буква сдвигается на заданное число n позиций вправо. Пробелы, знаки препинания не меняются. Например, для n = 1.
# a → b,   b → c,    p → q,    y → z,    z V a
# A → B,   B → C,   Z → A
# Т.е. заголовок функции будет def code(string, n):
# В качестве результата печатается сдвинутая строка.

alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_lower = alphabet_upper.lower()


def code(str, n):
    result = ""
    for i in range(len(str)):
        index = alphabet_upper.find(str[i])
        if index != -1:
            index += n
            if index > len(alphabet_upper):
                result += alphabet_upper[index - len(alphabet_upper)]
            else:
                result += alphabet_upper[index]
        else:
            index = alphabet_lower.find(str[i])
            if index != -1:
                index += n
                if index > len(alphabet_lower):
                    result += alphabet_lower[index - len(alphabet_lower)]
                else:
                    result += alphabet_lower[index]
            else:
                result += str[i]
    return result


temp = "aAyYzZbF"

print(code(temp, 3))
