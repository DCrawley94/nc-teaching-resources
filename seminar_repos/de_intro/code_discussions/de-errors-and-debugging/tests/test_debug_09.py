from src.exercises.debug_me_09 import add_numbers
import pytest


@pytest.mark.skip()
def test_returns_correct_value():
    expected_1 = 4
    result_1 = add_numbers("2", "2")
    assert result_1 == expected_1

    expected_2 = 10
    result_2 = add_numbers("5", "5")
    assert result_2 == expected_2

    expected_3 = 1500
    result_3 = add_numbers("750", "750")
    assert result_3 == expected_3
