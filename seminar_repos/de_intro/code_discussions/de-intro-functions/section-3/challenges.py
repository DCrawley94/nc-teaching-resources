import pytest


# Exercise 3
# This function should take any number of arguments and return the number of
#  arguments passed into the function
def how_many_arguments():
    pass


@pytest.mark.skip()
def test_how_many_arguments():
    assert how_many_arguments("a", "b", "c") == 3
    assert how_many_arguments() == 0
    assert how_many_arguments(1, 2, 3, 4, 5) == 5
    assert how_many_arguments("the", "meaning", "of", "life", "is", 42) == 6


# Exercise 4
# This function should take a dictionary representing a coin machine and a
#  string representing a coin as its arguments

# A coin machine object will take this form:
# {
#   "1p": 0,
#   "2p": 0,
#   "5p": 0,
#   "10p": 0
# }

# You should 'add the provided coin to the machine by altering the associated
#  key and returning the updated coin machine
def update_coin_machine():
    pass


@pytest.mark.skip()
def test_update_coin_machine():
    assert update_coin_machine({"1p": 0, "2p": 0, "5p": 0, "10p": 0}, "1p") == {
        "1p": 1,
        "2p": 0,
        "5p": 0,
        "10p": 0,
    }
    assert update_coin_machine({"1p": 0, "2p": 0, "5p": 0, "10p": 0}, "2p") == {
        "1p": 0,
        "2p": 1,
        "5p": 0,
        "10p": 0,
    }
    assert update_coin_machine({"1p": 0, "2p": 3, "5p": 0, "10p": 0}, "2p") == {
        "1p": 0,
        "2p": 4,
        "5p": 0,
        "10p": 0,
    }
    assert update_coin_machine({"1p": 0, "2p": 3, "5p": 10, "10p": 0}, "5p") == {
        "1p": 0,
        "2p": 3,
        "5p": 11,
        "10p": 0,
    }
    assert update_coin_machine({"1p": 0, "2p": 3, "5p": 10, "10p": 0}, "10p") == {
        "1p": 0,
        "2p": 3,
        "5p": 10,
        "10p": 1,
    }


# Exercise 6
# This function should take any value as an argument, and return true if it is
#  falsy, and false otherwise
def is_falsy():
    pass


@pytest.mark.skip()
def test_is_falsy():
    assert is_falsy(False) == True
    assert is_falsy(True) == False
    assert is_falsy("") == True
    assert is_falsy(0) == True
    assert is_falsy({}) == True
    assert is_falsy({"a": 1}) == False
    assert is_falsy([]) == True
    assert is_falsy([1, 2, 3]) == False
    assert is_falsy(None) == True
