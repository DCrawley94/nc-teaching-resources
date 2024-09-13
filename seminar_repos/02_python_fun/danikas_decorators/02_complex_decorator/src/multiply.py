"""
Create a decorator that will multiply the decorated function's output
by a given number and return that result of that multiplication.

@multiply(3)
def my_maths_func():
    return 4 + 2

my_maths_func = multiply(3)(my_maths_func)

my_maths_func() # 18
"""


def multiply(num):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            return num * func(*args)

        return inner_wrapper

    return outer_wrapper
