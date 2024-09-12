from src.multiply import multiply
import types

# Note: some tests will be brittle if you don't account for returning a number
#  (as it isn't technically needed until you do maths)

# Note: before embarking on tdd make sure you've explained
# what is happening under the surface when we pass an arg in (manually invocation)
# so students know what to test


def test_multiply_returns_a_function():
    result = multiply(3)
    assert type(result) == types.FunctionType
    # Could also be checked using callable function


def test_multiply_first_returned_func_returns_a_func():
    def test_func():
        pass
    result = multiply(3)(test_func)
    assert type(result) == types.FunctionType


def test_multiply_calls_decorated_func_once():
    count = 0

    @multiply(3)
    def test_func():
        nonlocal count
        count += 1
        return 0

    test_func()

    assert count == 1


def test_multiply_calls_decorated_func_with_args():

    passed_args = []

    @multiply(2)
    def mock_func(x):
        passed_args.append(x)
        return 0

    mock_func(1)
    assert passed_args == [1]


def test_multiply_calls_decorated_func_with_kwargs():

    passed_args = []

    @multiply(2)
    def mock_func(first, second):
        passed_args.append([first, second])
        return 0

    mock_func(first='Danika', second='Lewis')
    assert passed_args == [['Danika', 'Lewis']]


def test_multiply_returns_output_of_func_multiplied_by_given_number():

    @multiply(2)
    def mock_func1():
        return 32

    result1 = mock_func1()

    assert result1 == 64

    @multiply(5)
    def mock_func2():
        return 12

    result2 = mock_func2()

    assert result2 == 60
