import pytest

# In this function, you need to find out which letter is missing. But you
#  can't use a reference lookup table (i.e. no list or dictionary with the
#  whole alphabet in it) so you will have think outside the box!
# This function needs to take a list and needs to return the letter it is
#  missing.
# You will always get a sorted list of consecutive letters, and it will
#  always have exactly one letter missing. The length of the list will always
#  be at least 2. The list will always contain letters in only one case.


def find_missing_letter(letters):
    pass


def test_find_missing_letter_returns_an_empty_string_if_no_letters_are_missing():
    assert find_missing_letter(["A", "B", "C", "D", "E"]) == ""


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_find_missing_letter_returns_a_missing_capital_letter():
    assert find_missing_letter(["A", "B", "C", "E"]) == "D"


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_find_missing_letter_returns_a_missing_lower_case_letter():
    assert find_missing_letter(["e", "f", "g", "i"]) == "h"
