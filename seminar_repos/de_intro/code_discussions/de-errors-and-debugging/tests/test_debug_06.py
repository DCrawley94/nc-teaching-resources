from src.exercises.debug_me_06 import add_to_list
import pytest


@pytest.mark.skip()
def test_returns_correct_list_values():
    addition = 'Just have a top notch day'
    expected = [
        'Eat a hearty breakfast',
        'Enjoy some art',
        'Chase a flamingo',
        'Throw a bagel',
        'Just have a top notch day'
    ]
    result = add_to_list(addition)
    assert result == expected
