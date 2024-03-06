import pytest

# This function that accepts a string of any length, and replaces each letter
#  within each word with the corresponding index that that letter has in the
#  alphabet.
# You must have a space between each index number, and do NOT need to account
#  extra for spaces between words.


def alphabet_replace(string):
    pass


def test_alphabet_replace_returns_the_letters_in_a_single_word_with_codes():
    assert alphabet_replace("code") == "3 15 4 5"


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_alphabet_replace_is_case_insensitive():
    assert alphabet_replace("Northcoders") == "14 15 18 20 8 3 15 4 5 18 19"


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_alphabet_replace_ignores_spaces_between_words():
    assert alphabet_replace(
        "expert programming") == "5 24 16 5 18 20 16 18 15 7 18 1 13 13 9 14 7"
