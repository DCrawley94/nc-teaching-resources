from test_api.checks import run_test, skip_test, format_err_msg

# Exercise 3
# This function should take any number of arguments and return the number of
#  arguments passed into the function


def how_many_arguments():
    pass


@run_test
def test_how_many_arguments():
    assert how_many_arguments("a", "b", "c") == 3, \
        format_err_msg(3, how_many_arguments("a", "b", "c"))

    assert how_many_arguments() == 0, \
        format_err_msg(0, how_many_arguments())

    assert how_many_arguments(1, 2, 3, 4, 5) == 5, \
        format_err_msg(5, how_many_arguments(1, 2, 3, 4, 5))

    assert how_many_arguments("the", "meaning", "of", "life", "is", 42) == 6, \
        format_err_msg(8, how_many_arguments(
            "the", "meaning", "of", "life", "is", 42))


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


@skip_test
def test_update_coin_machine():
    assert update_coin_machine(
        {"1p": 0, "2p": 0, "5p": 0, "10p": 0}, "1p"
    ) == {"1p": 1, "2p": 0, "5p": 0, "10p": 0}, \
        format_err_msg(
            {"1p": 1, "2p": 0, "5p": 0, "10p": 0},
            update_coin_machine({"1p": 0, "2p": 0, "5p": 0, "10p": 0}, "1p"))

    assert update_coin_machine(
        {"1p": 0, "2p": 0, "5p": 0, "10p": 0}, "2p"
    ) == {"1p": 0, "2p": 1, "5p": 0, "10p": 0}, \
        format_err_msg(
            {"1p": 0, "2p": 1, "5p": 0, "10p": 0},
            update_coin_machine({"1p": 0, "2p": 0, "5p": 0, "10p": 0}, "2p"))

    assert update_coin_machine(
        {"1p": 0, "2p": 3, "5p": 0, "10p": 0}, "2p"
    ) == {"1p": 0, "2p": 4, "5p": 0, "10p": 0}, \
        format_err_msg(
            {"1p": 0, "2p": 4, "5p": 0, "10p": 0},
            update_coin_machine({"1p": 0, "2p": 3, "5p": 0, "10p": 0}, "2p"))

    assert update_coin_machine(
        {"1p": 0, "2p": 3, "5p": 10, "10p": 0}, "5p"
    ) == {"1p": 0, "2p": 3, "5p": 11, "10p": 0}, \
        format_err_msg(
            {"1p": 0, "2p": 3, "5p": 11, "10p": 0},
            update_coin_machine({"1p": 0, "2p": 3, "5p": 10, "10p": 0}, "5p"))

    assert update_coin_machine(
        {"1p": 0, "2p": 3, "5p": 10, "10p": 0}, "10p"
    ) == {"1p": 0, "2p": 3, "5p": 10, "10p": 1}, \
        format_err_msg(
            {"1p": 0, "2p": 3, "5p": 10, "10p": 1},
            update_coin_machine({"1p": 0, "2p": 3, "5p": 10, "10p": 0}, "10p"))


# Exercise 6
# This function should take any value as an argument, and return true if it is
#  falsy, and false otherwise
def is_falsy():
    pass


@skip_test
def test_is_falsy():
    assert is_falsy(False) is True, format_err_msg(True, is_falsy(False))
    assert is_falsy(True) is False, format_err_msg(False, is_falsy(True))
    assert is_falsy("") is True, format_err_msg(True, is_falsy(''))
    assert is_falsy(0) is True, format_err_msg(True, is_falsy(0))
    assert is_falsy({}) is True, format_err_msg(True, is_falsy({}))
    assert is_falsy({"a": 1}) is False, \
        format_err_msg(False, is_falsy({"a": 1}))
    assert is_falsy([]) is True, format_err_msg(True, is_falsy([]))
    assert is_falsy([1, 2, 3]) is False, \
        format_err_msg(False, is_falsy([1, 2, 3]))
    assert is_falsy(None) is True, format_err_msg(True, is_falsy(None))


if __name__ == "__main__":
    test_how_many_arguments()
    test_update_coin_machine()
    test_is_falsy()
