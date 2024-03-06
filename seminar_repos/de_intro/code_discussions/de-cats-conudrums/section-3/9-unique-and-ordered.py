import pytest

# Implement a function which takes as an argument a sequence and returns a
#  list of items without any elements with the same value next to each other
#  and preserving the original order of elements.
# The function should be able to to work with both strings and lists, and
#  should return an list.


def unique_and_ordered():
    pass


def test_unique_and_ordered_returns_unique_ordered_numbers_from_an_list():
    assert unique_and_ordered(
        [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 1, 1]) == [1, 2, 3, 1]


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_unique_and_ordered_returns_unique_ordered_letters_from_a_string():
    assert unique_and_ordered("nnoorrtthhccooddeerrss") == [
        "n", "o", "r", "t", "h", "c", "o", "d", "e", "r", "s"]


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_unique_and_ordered_is_case_sensitive_for_strings():
    assert unique_and_ordered("AaAAABBBCCCc") == ["A", "a", "A", "B", "C", "c"]
