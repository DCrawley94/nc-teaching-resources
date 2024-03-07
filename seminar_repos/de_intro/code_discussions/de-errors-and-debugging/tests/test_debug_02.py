from src.exercises.debug_me_02 import return_dog_string
import pytest


@pytest.mark.skip()
def test_returns_correct_value():
    expected = 'Hello, I am a fancy talking dog and my name is Mackerel.'
    result = return_dog_string()
    assert result == expected
