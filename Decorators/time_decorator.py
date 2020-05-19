from time import time
from functools import wraps
from math import factorial


def time_decorator(some_func):
    @wraps(some_func)
    def inner(*args, **kwargs):
        start_time = time()
        res = some_func(*args, **kwargs)
        print(f"Done in {(time() - start_time)} seconds")
        return res

    return inner


@time_decorator
def my_factorial(x): return factorial(x)


print(my_factorial(2))
