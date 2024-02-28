def validate_arg(data_type):
    """
    Decorator should be applied to a function that accepts a single argument.
    It will check that the data type of the argument provided to the decorated
    function is correct and only invoke the function if that is the case. If
    the argument is the correct data type then return value of func should be
    returned. Otherwise a string of "Incorrect data type" should be returned.
    """
    def outer_wrapper(func):
        def inner_wrapper(arg):
            if isinstance(arg, data_type):
                return func(arg)
            else:
                return "Incorrect data type"
        return inner_wrapper
    return outer_wrapper


def test_validate_arg_returns_function():
    assert callable(validate_arg(str))


def test_validate_arg_first_wrapper_func_returns_function():
    def test_func(x):
        pass

    assert callable(validate_arg(str)(test_func))


def test_validate_arg_return_func_output_if_correct_data_type():
    @validate_arg(str)
    def say_hello(name):
        return f"Hello {name}"

    assert say_hello('Alex') == "Hello Alex"


def test_validate_arg_returns_error_message_incorrect_data_type():
    @validate_arg(str)
    def say_hello(name):
        return f"Hello {name}"

    assert say_hello(5) == "Incorrect data type"

# Can also highlight that we can test with a mock to make sure that a function
# is definitely invoked/not invoked

# E.G:


def test_validate_arg_does_not_invoke_function_if_wrong_data_type():
    call_count = 0

    @validate_arg(str)
    def mock_func(x):
        nonlocal call_count
        call_count += 1

    mock_func(True)

    assert call_count == 0

# Can extend on this with multiple args/data types if there's time
