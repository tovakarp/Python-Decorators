from functools import wraps


def function_calls(some_func):
    count = 0

    @wraps(some_func)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1

        res = some_func(*args, **kwargs)
        print(f'{some_func.__name__} was called {count} times')
        return res

    return inner


@function_calls
def add(x, y): return x + y


@function_calls
def sub(x, y): return x - y


add(1, 2)
add(1, 2)
add(1, 2)

sub(20, 10)

add(1, 2)
add(1, 2)
