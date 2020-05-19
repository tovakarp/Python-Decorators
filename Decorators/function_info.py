import inspect
import itertools
from functools import wraps
from random import randint


def function_info(some_func):
    @wraps(some_func)
    def inner(*args, **kwargs):
        print(f"Function name: {some_func.__name__}")
        largs = [x for x in args]
        lkwargs = list(map(lambda v: f'{v} = {kwargs[v]}', kwargs))
        #{some_func.__code__.co_varnames[:some_func.__code__.co_argcount][::-1]}
        print(f"Function arguments: {largs + lkwargs}")

        res = some_func(*args, **kwargs)

        print(type(res), res)

    return inner


@function_info
def do_someting(a, *args, **kwargs): return None if not len(args) and not len(kwargs) else kwargs or args[
    randint(0, len(args) - 1)]


do_someting(1, 2, kwarg=3, kwarg2="some_thing")
