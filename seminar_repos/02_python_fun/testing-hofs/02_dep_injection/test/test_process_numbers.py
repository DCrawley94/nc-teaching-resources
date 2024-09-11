from src.process_numbers import process_numbers
from unittest.mock import Mock
import pytest


def test_process_numbers_returns_empty_list_when_passed_empty_list():
    def test_filter_fn(val):
        return val

    assert process_numbers([], test_filter_fn) == 0


def test_process_numbers_applies_given_filter_function_to_the_input_list():
    has_been_called = False
    call_list = []

    def test_filter_fn(input_list):
        nonlocal has_been_called
        has_been_called = True
        call_list.append(input_list)
        return [1, 3, 5]

    assert process_numbers([1, 2, 3, 4, 5], test_filter_fn) == 9
    assert has_been_called is True
    assert call_list == [[1, 2, 3, 4, 5]]


def test_process_function_applies_both_filter_and_tranform_funcs():
    filter_has_been_called = False
    filter_call_list = []

    def test_filter_fn(input_list):
        nonlocal filter_has_been_called
        filter_has_been_called = True
        filter_call_list.append(input_list)
        return [1, 3, 5]

    transform_has_been_called = False
    transform_call_list = []

    def test_transform_fn(input_list):
        nonlocal transform_has_been_called
        transform_has_been_called = True
        transform_call_list.append(input_list)
        return [2, 6, 10]

    assert process_numbers([1, 2, 3, 4, 5], test_filter_fn, test_transform_fn) == 18

    assert transform_has_been_called is True
    assert transform_call_list == [[1, 3, 5]]


@pytest.mark.skip()
def test_process_numbers_returns_processed_numbers():
    # This could be a pre-written test that can be refactored as you add more
    #   Mock tests
    test_num_list = [1, 2, 3, 4, 5]
    expected_return = 18

    assert process_numbers(test_num_list) == expected_return


@pytest.mark.skip()
def test_filter_function_is_invoked_with_numbers_list():
    test_num_list = [1, 2, 3, 4, 5]
    test_filter_fn = Mock(return_value=[2, 4])

    process_numbers(test_num_list, test_filter_fn)

    test_filter_fn.assert_called_with(test_num_list)


@pytest.mark.skip()
def test_transform_function_is_invoked_with_filtered_numbers():
    test_num_list = [1, 2, 3, 4, 5]
    filtered_numbers = [2, 4]

    test_filter_fn = Mock(return_value=filtered_numbers)
    test_transform_fn = Mock(return_value=[1, 2])

    process_numbers(test_num_list, test_filter_fn, test_transform_fn)

    test_transform_fn.assert_called_with(filtered_numbers)
