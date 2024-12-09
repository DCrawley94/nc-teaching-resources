from src.utils import filter_odd_numbers, double_numbers


def test_filter_odd_numbers_empty_list():
    assert filter_odd_numbers([]) == []


def test_filter_odd_numbers_returns_list_containing_only_odds():
    assert filter_odd_numbers([1, 3, 5]) == [1, 3, 5]


def test_filter_odd_numbers_returns_empty_list_when_passed_even_nums():
    assert filter_odd_numbers([2, 4, 6]) == []


def test_filter_odd_numbers_mixed_list():
    assert filter_odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5]


def test_double_numbers_empty_list():
    assert double_numbers([]) == []


def test_double_numbers_returns_all_numbers_doubled():
    assert double_numbers([1, 2, 3]) == [2, 4, 6]
