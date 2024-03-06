import pytest

# This function takes an list of words and returns an list containing only
#  the palindromes.
# A palindrome is a word that is spelled the same way backwards.
# E.g. ['foo', 'racecar', 'pineapple', 'porcupine', 'tacocat'] =>
#  ['racecar', 'tacocat']


def get_palindromes(words):
    pass


def test_get_palindromes_returns_empty_list_when_passed_empty_list():
    assert get_palindromes([]) == []


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_get_palindromes_identifies_palindromes():
    assert get_palindromes(["racecar"]) == ["racecar"]
    assert get_palindromes(["racecar", "racecar"]) == ["racecar", "racecar"]


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_get_palindromes_ignores_non_palindromes():
    assert get_palindromes(["racecar", "kayak", "tacocat"]) == [
        "racecar", "kayak", "tacocat"]
    assert get_palindromes(["pineapple", "pony", "racecar"]) == ["racecar"]


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_get_palindromes_returns_empty_list_when_passed_no_palindromes():
    assert get_palindromes(["pineapple", "watermelon", "pony"]) == []
