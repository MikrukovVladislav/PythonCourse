#
#    Дан список чисел.  Превратить его в список суммы цифр каждого числа. Пример входа: lst = [123, 234, 345, 456]
#    Вывод: [6, 9, 12, 15]
#    При решении используйте map и lambda

lst = [123, 234, 345, 456]

test_lambda = lambda arg: sum(list(map(lambda x:(int(x)),str(arg))))

result = list(map(test_lambda, lst))

print(result)
