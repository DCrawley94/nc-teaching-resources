def double(func):
    def wrapper():
        original_return = func()
        return original_return * 2
    return wrapper


def test_double_returns_a_new_function():
    def test_func(x):
        pass

    assert callable(double(test_func))


def test_double_decorator_doubles_output_of_decorated_func():
    @double
    def quick_maths():
        return 2 + 2 - 1

    assert quick_maths() == 6
