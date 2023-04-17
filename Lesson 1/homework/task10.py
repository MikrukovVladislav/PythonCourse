#Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
#Дан номер единицы массы и масса тела M в этих единицах (вещественное число). Вывести массу данного тела в килограммах.
# Данную задачу нужно решить с помощью конструкции  match  (Python v3.10)


# Пример:
# Введите единицу массы тела
#       1 - килограмм
#       2 — миллиграмм
#       3 — грамм
#       4 — тонна
#       5 — центнер
#>4

#Введите  массу тела
#>1

#Ответ: 1000 кг

def select_type_weight(types):
    match types:
        case 1: return 1
        case 2: return 0.000001
        case 3: return 0.001
        case 4: return 1000
        case 5: return 100

weight = float(input("Введите массу тела: "))
type_weight = int(input("Введите тип единиц массы тела: "))

print("Ответ: " + str(weight*select_type_weight(type_weight)) + " кг")