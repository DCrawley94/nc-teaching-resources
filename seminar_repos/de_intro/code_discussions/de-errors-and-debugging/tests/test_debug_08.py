from src.exercises.debug_me_08 import return_last_digit
import pytest


@pytest.mark.skip()
def test_returns_correct_number():
    expected_1 = 1
    result_1 = return_last_digit(1)
    assert result_1 == expected_1

    expected_2 = 8
    result_2 = return_last_digit(28)
    assert result_2 == expected_2

    expected_3 = 6
    result_3 = return_last_digit(456)
    assert result_3 == expected_3

    expected_4 = 3
    result_4 = return_last_digit(7653)
    assert result_4 == expected_4
