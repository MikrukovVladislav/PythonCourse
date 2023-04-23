#
# Реализовать декоратор который подсчитывает время выполнения функции.
import time


def dec_timer_func(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func()
        print("[test_func]: time is " + str(time.time() - start_time))

    return wrapper


@dec_timer_func
def test_func():
    time.sleep(2)
    return ""


test_func()
