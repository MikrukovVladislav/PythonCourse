#
# Напишите программу с использованием конструкции try-except, которая принимает на вход название текстового файла и выводит его содержимое.
# Если файла с данным названием нет в папке с программой, программа должна вывести текст:
#
# Файл не найден
#
# На вход программе подается название текстового файла.
# Программа должна вывести содержимое файла с введенным названием или соответствующий текст, если файла с данным названием
# нет в папке с программой.
#
# Примечание 1. Название подаваемого файла уже содержит расширение.
#
# Примечание 2. При открытии файла используйте явное указание кодировки UTF-8.

filename = str(input("Введите название файла: "))

try:
    with open(filename, encoding="UTF-8") as f:
        print(f.read())
except FileNotFoundError as e:
    print("File not found")
