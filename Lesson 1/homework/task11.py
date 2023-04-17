#Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.
import random

nums = set()

for i in range(10):
    nums.add(random.randint(-10000, 10000))
    #nums.append(random.randint(-10000, 10000))

a = list(nums)

print(nums)
print(type(nums))

for i in range(10):
    a[i] += 1

print(a)
print(type(a))