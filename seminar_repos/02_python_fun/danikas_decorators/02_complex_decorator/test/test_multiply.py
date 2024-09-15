from src.multiply import multiply


# multiply should return a function
def test_multiply_returns_a_function():
    output = multiply(3)
    assert callable(output)


# returned function should also return a a function
def test_returned_function_returns_second_func():
    def dummy_func():
        return 5

    output = multiply(3)(dummy_func)
    assert callable(output)


# decorated function is called
def test_multiply_calls_decorated_function():
    has_been_called = False

    @multiply(3)
    def test_func():
        nonlocal has_been_called
        has_been_called = True
        return 5

    test_func()

    assert has_been_called


# final function should return multiplied value
def test_multiply_returns_result_of_decorated_func_multiplied_by_given_number():
    @multiply(2)
    def test_func():
        return 5

    output = test_func()

    assert output == 10


def test_multiply_function_can_decorate_functions_that_accept_args():
    @multiply(5)
    def test_func(a, b):
        return a + b

    output = test_func(2, 2)

    assert output == 20


# my_maths_func = multiply(3)
# my_maths_func = decorated_multiply(my_maths_func)
# my_maths_func() # 18
