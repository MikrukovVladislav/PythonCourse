#На вход подается предложение из нескольких слов. Слова разделены пробелами.
# Напечатайте самое длинное слово в этом предложении.

string = input("Введите предложение: ")

a = string.split(" ")

index = 0

for i in range(len(a)):
    if len(a[index]) < len(a[i]):
        index = i

print(a)
print(index)
print(a[index])