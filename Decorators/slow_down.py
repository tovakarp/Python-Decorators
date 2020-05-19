from functools import wraps
from time import sleep


def slow_down(some_func):
    @wraps(some_func)
    def inner(*args, **kwargs):
        sleep(1)
        res = some_func(*args, **kwargs)
        return res

    return inner


@slow_down
def add(x, y): return x + y


print(add(2, 3))
