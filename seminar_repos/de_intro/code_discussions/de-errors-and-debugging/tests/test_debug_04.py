from src.exercises.debug_me_04 import access_dictionary
import pytest


@pytest.mark.skip()
def test_accesses_correct_value():
    expected_1 = "Spelling with cbeebies"
    result_1 = access_dictionary("Alex")
    assert result_1 == expected_1

    expected_2 = "The Simpsons"
    result_2 = access_dictionary("Danika")
    assert result_2 == expected_2

    expected_3 = "My Little Pony"
    result_3 = access_dictionary("Simon")
    assert result_3 == expected_3

    expected_4 = "Battlestar galactica"
    result_4 = access_dictionary("Kyle")
    assert result_4 == expected_4

    expected_5 = "Rick and Morty"
    result_5 = access_dictionary("Chon")
    assert result_5 == expected_5
