from test_api.checks import run_test, skip_test, format_err_msg

# QUESTION 2
# This function should take a string as an argument and return True if
#  every letter is upper case and False if at least one character is not

def is_all_upper_case(string):
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


@run_test
def test_collect_the_vowels():
    assert collect_the_vowels("a") == "a", \
        format_err_msg('a', collect_the_vowels("a"))
    assert collect_the_vowels("bcd") == "", \
        format_err_msg('', collect_the_vowels("bcd"))
    assert collect_the_vowels("bcdepiaouk") == "eiaou", \
        format_err_msg('eiaou', collect_the_vowels("bcdepiaouk"))



if __name__ == "__main__":
    test_is_all_upper_case()
    test_collect_the_vowels()
