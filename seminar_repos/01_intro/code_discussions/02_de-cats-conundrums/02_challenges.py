from test_api.checks import run_test, skip_test, format_err_msg
import re

# QUESTION 2
# This function should take a string as an argument and return True if
#  every letter is upper case and False if at least one character is not


def is_all_upper_case(string):
    # check if all characters contained within the string are uppercase

    # return string == string.upper()
    return string.isupper()


@run_test
def test_is_all_upper_case():
    assert is_all_upper_case("hello") is False, format_err_msg(
        False, is_all_upper_case("hello")
    )
    assert is_all_upper_case("WORLD") is True, format_err_msg(
        True, is_all_upper_case("WORLD")
    )
    assert is_all_upper_case("HI Mabel") is False, format_err_msg(
        False, is_all_upper_case("HI Mabel")
    )


# QUESTION 3
# This function should take a string as its argument and return a
#  string consisting of all vowels found in the input (retaining the order)


# def collect_the_vowels(str):
#     # create a new string to cntain the vowel
#     vowels_found = ""

#     # iterate over original
#     for char in str:
#         # check if char is a vowel - add to vowel string
#         if char in "aeiou":
#             vowels_found += char

#     # return vowel string
#     return vowels_found


# def collect_the_vowels(str):
#     vowels = "aeiou"

#     return "".join([char for char in str if char in vowels])


def collect_the_vowels(str):
    vowel_regex = re.compile(r"[aeiou]")
    found_vowels = vowel_regex.findall(str)

    return "".join(found_vowels)


@run_test
def test_collect_the_vowels():
    assert collect_the_vowels("a") == "a", format_err_msg("a", collect_the_vowels("a"))
    assert collect_the_vowels("bcd") == "", format_err_msg(
        "", collect_the_vowels("bcd")
    )
    assert collect_the_vowels("bcdepiaouk") == "eiaou", format_err_msg(
        "eiaou", collect_the_vowels("bcdepiaouk")
    )


if __name__ == "__main__":
    test_is_all_upper_case()
    test_collect_the_vowels()
