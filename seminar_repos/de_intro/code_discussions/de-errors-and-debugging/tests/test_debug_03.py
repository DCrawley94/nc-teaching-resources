from src.exercises.debug_me_03 import return_mentor_string
import pytest


@pytest.mark.skip()
def test_returns_greeting():
    expected_1 = "Hello Alex!"
    result_1 = return_mentor_string("Alex")
    assert result_1 == expected_1

    expected_2 = "Hello Danika!"
    result_2 = return_mentor_string("Danika")
    assert result_2 == expected_2
