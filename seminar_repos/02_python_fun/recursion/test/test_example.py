from src.example import count_ice_creams
import pytest


def test_empty_list_returns_0():
    assert count_ice_creams([]) == 0


def test_none_nested_list_no_ice_cream_returns_0():
    input_1 = ["not ice cream", "egg", "hello northcoders"]
    expected = 0

    result = count_ice_creams(input_1)

    assert result == expected


def test_none_nested_list_with_ice_cream_returns_count_of_ice_creams():
    input_1 = ["ice cream", "egg", "hello northcoders", "ice cream"]
    expected = 2

    result = count_ice_creams(input_1)

    assert result == expected


def test_single_nested_list_with_single_ice_cream():
    input_1 = [["ice cream"]]
    expected = 1

    result = count_ice_creams(input_1)

    assert result == expected


def test_multiple_nested_lists():
    input_1 = [["ice cream"], ["ice cream"]]
    expected = 2

    result = count_ice_creams(input_1)

    assert result == expected


def test_multiple_levels_of_nesting():
    input_1 = [[["ice cream"]]]
    expected = 1

    result = count_ice_creams(input_1)

    assert result == expected


def test_multiple_nested_items_varied_nesting():
    varied_nesting_search = [
        ["ice cream"],
        "sadness",
        [["ice cream"], "sadness"],
        [[["ice cream", "sadness"], "ice cream"]],
    ]
    expected = 4

    result = count_ice_creams(varied_nesting_search)

    assert result == expected
