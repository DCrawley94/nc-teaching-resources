from src.exercises.debug_me_07 import shopping_trip
import pytest


@pytest.mark.skip()
def test_returns_message_enough_money():
    expected_1 = "You can buy Danika's tears!"
    result_1 = shopping_trip(50, "Danika's tears")
    assert result_1 == expected_1

    expected_2 = "You can buy Kyle's house!"
    result_2 = shopping_trip(50, "Kyle's house")
    assert result_2 == expected_2


@pytest.mark.skip()
def test_returns_message_not_enough_money():
    expected = "You can't afford Simon's beard..."
    result = shopping_trip(50, "Simon's beard")
    assert result == expected
