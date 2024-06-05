from test_api.checks import run_test, skip_test, format_err_msg


# QUESTION 2
# This function should take a string as an argument and return True if
#  every letter is upper case and False if at least one character is not

def is_all_upper_case():
    pass


@skip_test
def test_is_all_upper_case():
    assert is_all_upper_case("hello") is False, \
        format_err_msg(False, is_all_upper_case("hello"))
    assert is_all_upper_case("WORLD") is True, \
        format_err_msg(True, is_all_upper_case("WORLD"))
    assert is_all_upper_case("HI Mabel") is False, \
        format_err_msg(False, is_all_upper_case("HI Mabel"))


# QUESTION 3
# This function should take a string as its argument and return a
#  string consisting of all vowels found in the input (retaining the order)

def collect_the_vowels(str):
    pass


@skip_test
def test_collect_the_vowels():
    assert collect_the_vowels("a") == "a", \
        format_err_msg('a', collect_the_vowels("a"))
    assert collect_the_vowels("bcd") == "", \
        format_err_msg('', collect_the_vowels("bcd"))
    assert collect_the_vowels("bcdepiaouk") == "eiaou", \
        format_err_msg('eiaou', collect_the_vowels("bcdepiaouk"))


# QUESTION 4
# This function should take two arguments, a list and an index, and return
#  the element at that specified index

# The index provided may be equal to or greater than the length of the
#  given list. In this case, rather than counting past the end of the
#  list where there are no values, the indexing should be considered to
#  "loop back around" and continue from the start of the list

# For examples of this behaviour, look at the second group of tests below

def access_item(list, index):
    pass


@skip_test
def test_access_item_retrieves_item_when_passed_index_less_than_list_len():
    assert access_item(["a", "b", "c", "d"], 2) == "c", \
        format_err_msg("c", access_item(["a", "b", "c", "d"], 2))
    assert access_item(["a", "b", "c", "d"], 0) == "a", \
        format_err_msg("a", access_item(["a", "b", "c", "d"], 0))
    assert access_item(["a", "b", "c", "d"], 3) == "d", \
        format_err_msg("d", access_item(["a", "b", "c", "d"], 3))


@skip_test
def test_access_item_retrieves_item_when_passed_index_greater_or_equal_to_list_len():
    assert access_item(["a", "b", "c", "d"], 4) == "a", \
        format_err_msg("a", access_item(["a", "b", "c", "d"], 4))
    assert access_item(["a", "b", "c", "d"], 6) == "c", \
        format_err_msg("c", access_item(["a", "b", "c", "d"], 6))
    assert access_item(["a", "b", "c", "d"], 10) == "c", \
        format_err_msg("c", access_item(["a", "b", "c", "d"], 10))



if __name__ == "__main__":
    test_is_all_upper_case()
    test_collect_the_vowels()
    test_access_item_retrieves_item_when_passed_index_less_than_list_len()
    test_access_item_retrieves_item_when_passed_index_greater_or_equal_to_list_len()
