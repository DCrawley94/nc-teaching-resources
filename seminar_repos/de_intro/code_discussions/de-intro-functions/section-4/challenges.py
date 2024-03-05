import pytest


# Exercise 0
# Write a function, check_if_key_exists, that takes a dictionary and a key as
#  its arguments
# It should return True if the dictionary contains the provided key,
#  False otherwise


def test_check_if_key_exists():
    assert check_if_key_exists({"name": "jonny", "age": 32}, "name") == True
    assert check_if_key_exists({"name": "jonny", "age": 32}, "age") == True
    assert check_if_key_exists({"name": "jonny", "age": 32}, "pets") == False


# Exercise 2
# Write a function, get_first_n_items, that takes two arguments, a list and
#  a number 'n'
# It should return a new list containing the first 'n' items of the given list

@pytest.mark.skip()
def test_get_first_n_items():
    assert get_first_n_items(["a", "b", "c", "d"], 2) == ["a", "b"]
    assert get_first_n_items(["apple", "banana", "pear", "kiwi"], 0) == []
    assert get_first_n_items(["apple", "banana", "pear", "kiwi"], 3) == [
        "apple",
        "banana",
        "pear",
    ]
