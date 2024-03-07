
from src.exercises.debug_me_01 import say_hello


def test_returns_correct_value():
    expected = 'Hello Data Engineers.'
    result = say_hello()
    assert result == expected
