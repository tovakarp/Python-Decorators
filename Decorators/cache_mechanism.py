from functools import wraps


def cache_mechanism(some_func):
    cache = {}

    @wraps(some_func)
    def inner(*args, **kwargs):
        nonlocal cache
        if args not in cache:
            cache[args] = some_func(*args, **kwargs)
        return cache[args]

    return inner


@cache_mechanism
def my_fibonacci(x): return 1 if x == 1 or x == 2 else my_fibonacci(x - 1) + my_fibonacci(x - 2)


print(my_fibonacci(6))
print(my_fibonacci(7))
print(my_fibonacci(6))
