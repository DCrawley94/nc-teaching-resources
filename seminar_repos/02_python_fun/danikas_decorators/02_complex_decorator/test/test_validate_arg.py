from src.validate_arg import validate_arg


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
