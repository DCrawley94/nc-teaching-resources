"""
Create a decorator that will multiply the decorated function's output
by a given number and return that result of that multiplication.

@multiply(3)
def my_maths_func():
    return 4 + 2

my_maths_func() # 18
"""


def multiply(num):
    def outer_wrapper(func):
        def inner_wrapper(*args):  # packs arguments into a tuple
            return func(*args) * num  # unpacks arguments into function call

        return inner_wrapper

    return outer_wrapper


@multiply(1)
def sum():
    pass
