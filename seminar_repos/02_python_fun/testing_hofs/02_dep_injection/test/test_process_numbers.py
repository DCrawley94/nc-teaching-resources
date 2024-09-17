from src.process_numbers import process_numbers
from unittest.mock import Mock


# Empty list - returns zero


def test_process_numbers_returns_zero_when_passed_empty_list():
    test_input = []

    def test_filter_fn(arg):
        return arg

    assert process_numbers(test_input, test_filter_fn) == 0


def test_process_numbers_should_invoke_filter_fn_with_given_list():
    test_input = [1]

    test_filter_fn = Mock(return_value=[1])

    assert process_numbers(test_input, test_filter_fn) == 1

    test_filter_fn.assert_called()
    test_filter_fn.assert_called_with([1])


def test_process_numbers_should_invoke_transformation_fn_with_filtered_list():
    test_input = [1, 2, 3, 4, 5]
    has_been_called = False

    def test_filter_fn(lst):
        return [1, 3, 5]

    def test_transform_fn(lst):
        nonlocal has_been_called
        has_been_called = True

        return [2, 6, 10]

    assert process_numbers(test_input, test_filter_fn, test_transform_fn) == 18
    assert has_been_called
