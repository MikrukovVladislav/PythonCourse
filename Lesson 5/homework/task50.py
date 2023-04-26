#
# Создайте декоратор, которые переводит все текстовые аргументы функции
# в верхний регистр и возвращает их в виде списка текстовых аргументов.

class Person:
    def benchmark(func):
        def wrapper(*args, **kwargs):
            # a = ""
            # for tmp in args:
            #     if isinstance(tmp, str):
            #         a += tmp + ", "

            a = [n.upper() for n in args if isinstance(n, str)]

            print(a)
            pass

        return wrapper

    @benchmark
    def fetch_webpage(*args):
        pass


a = Person()
a.fetch_webpage('https://google.com', 1, "234", "temP")
