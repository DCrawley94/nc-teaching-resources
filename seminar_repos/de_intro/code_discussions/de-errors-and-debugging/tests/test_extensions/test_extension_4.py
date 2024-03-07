from src.extension.extension_bug_4 import sum_sentence
import pytest


@pytest.mark.skip()
def test_returns_correct_string_when_passed_an_empty_list():
    expected = "The total cost of the fruits is £0"
    result = sum_sentence([])
    assert result == expected


@pytest.mark.skip()
def test_returns_correct_string_for_one_fruit():
    expected = "The total cost of the fruits is £5"
    result = sum_sentence([{"fruit": "apple", "cost": 5}])
    assert result == expected


@pytest.mark.skip()
def test_returns_correct_string_for_multiple_fruits():
    expected = "The total cost of the fruits is £33"
    result = sum_sentence([
        {"fruit": "red apple", "cost": 5},
        {"fruit": "poison apple", "cost": 20},
        {"fruit": "kiwi", "cost": 1},
        {"fruit": "tomato ;)", "cost": 2},
        {"fruit": "green apple", "cost": 5},
    ])
    assert result == expected
