from src.exercises.debug_me_05 import multiply_by_3
import pytest


@pytest.mark.skip()
def test_returns_expected_number():
    assert multiply_by_3(1) == 3
    assert multiply_by_3(2) == 6
    assert multiply_by_3(3) == 9
    assert multiply_by_3(4) == 12
