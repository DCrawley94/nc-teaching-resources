from test_api.checks import run_test, skip_test, format_err_msg

# Exercise 0
# Write a function, check_if_key_exists, that takes a dictionary and a key as
#  its arguments
# It should return True if the dictionary contains the provided key,
#  False otherwise


@run_test
def test_check_if_key_exists():
    assert check_if_key_exists({"name": "jonny", "age": 32}, "name") is True, \
        format_err_msg(
            True, check_if_key_exists({"name": "jonny", "age": 32}, "name"))

    assert check_if_key_exists({"name": "jonny", "age": 32}, "age") is True, \
        format_err_msg(
            True, check_if_key_exists({"name": "jonny", "age": 32}, "age"))

    assert check_if_key_exists(
        {"name": "jonny", "age": 32}, "pets") is False, \
        format_err_msg(
            False, check_if_key_exists({"name": "jonny", "age": 32}, "pets"))


# Exercise 2
# Write a function, get_first_n_items, that takes two arguments, a list and
#  a number 'n'
# It should return a new list containing the first 'n' items of the given list

@skip_test
def test_get_first_n_items():
    assert get_first_n_items(["a", "b", "c", "d"], 2) == ["a", "b"], \
        format_err_msg(["a", "b"], get_first_n_items(["a", "b", "c", "d"], 2))

    assert get_first_n_items(["apple", "banana", "pear", "kiwi"], 0) == [], \
        format_err_msg([], get_first_n_items(
            ["apple", "banana", "pear", "kiwi"], 0))

    assert get_first_n_items(["apple", "banana", "pear", "kiwi"], 3) == \
        ["apple", "banana", "pear"], \
        format_err_msg(["apple", "banana", "pear"], get_first_n_items(
            ["apple", "banana", "pear", "kiwi"], 3))


if __name__ == "__main__":
    test_check_if_key_exists()
    test_get_first_n_items()
