from src.multiply import multiply


def test_multiply_returns_function():
    result = multiply(3)

    assert callable(result)


def test_returned_func_returns_second_func():
    def quick_maths():
        return 2 + 2 - 1

    result = multiply(2)(quick_maths)

    assert callable(result)


def test_multiply_wrapper_calls_given_function_once():
    has_been_called = False

    @multiply(5)
    def test_func():
        nonlocal has_been_called
        has_been_called = True
        return 0

    test_func()

    assert has_been_called


def test_multiply_returns_the_multiplied_result():
    @multiply(2)
    def quick_maths():
        return 2 + 2 - 1

    result_1 = quick_maths()

    assert result_1 == 6


def test_multiply_invokes_given_function_when_function_accepts_args():
    passed_args = None

    @multiply(2)
    def mock_func(arg_1, arg_2):
        nonlocal passed_args
        passed_args = [arg_1, arg_2]
        return arg_1 + arg_2

    mock_func(1, 2)

    assert passed_args == [1, 2]
