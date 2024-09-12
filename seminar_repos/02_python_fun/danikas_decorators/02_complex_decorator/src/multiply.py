def multiply(num):
    def multiply_decorator(func):
        def wrapper_func(*args):
            output = func(*args)
            return output * num
        return wrapper_func
    return multiply_decorator


'''
Create a decorator that will multiply the decorated function’s output by a given value.

@multiply(3)
def my_maths_func():
    return 4 + 2

my_maths_func = multiply(3)(my_maths_func)

my_maths_func() # 18
'''
