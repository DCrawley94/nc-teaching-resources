import pytest

# QUESTION 1
# This function should take 2 strings and join them together with a space
#  in between.
# return this newly created string


def connect_strings():
    pass


def test_connect_strings():
    assert connect_strings("hello", "world") == "hello world"
    assert connect_strings("cat", "hoang") == "cat hoang"
    assert connect_strings("blue", "sky") == "blue sky"


# QUESTION 2
# This function should take a string as an argument and return a boolean
#  based on whether the word given ends with 'ing'

def check_word_ends_with_ing():
    pass


@pytest.mark.skip()
def test_check_word_ends_with_ing():
    assert check_word_ends_with_ing("doing") == True
    assert check_word_ends_with_ing("eating") == True
    assert check_word_ends_with_ing("cry") == False
    assert check_word_ends_with_ing("coder") == False


# QUESTION 3
# This function should take a string as an argument
# each string may end with a full-stop, exclamation mark, or question mark
# if the string doesn't end with punctuation, return the string with a
#  full-stop added at the end. Otherwise, return the string unchanged

def add_missing_punctuation():
    pass


@pytest.mark.skip()
def test_add_missing_punctuation():
    assert add_missing_punctuation("Hello there!") == "Hello there!"
    assert add_missing_punctuation("How's it going?") == "How's it going?"
    assert add_missing_punctuation("Yeah I'm good") == "Yeah I'm good."
    assert add_missing_punctuation("Nice") == "Nice."


# QUESTION 4
# This function should take two arguments a and b, and return the remainder
#  of the division of a / b

def get_remainder():
    pass


@pytest.mark.skip()
def test_get_remainder():
    assert get_remainder(10, 2) == 0
    assert get_remainder(119, 10) == 9
    assert get_remainder(50, 6) == 2


# QUESTION 5
# This function should take an dictionary and a key as its arguments and
#  return the value found at the provided key in the input dictionary
# If the key doesn't exist on the dictionary, this function should return a
#  string of "property not found"

def access_object(obj, key):
    pass


@pytest.mark.skip()
def test_access_object():
    assert access_object({"name": "nara", "age": 5}, "name") == "nara"
    assert access_object({"name": "nara", "age": 5}, "age") == 5
    assert access_object({"name": "nara", "age": 5},
                         "email") == "property not found"


# QUESTION 6
# In markdown files (e.g. 'README.md') we can denote words as bold by putting
#  two asterisks on either side of them, such as: **hello**
# This function should take an list of strings as an argument and return an
#  list consisting of the same strings but in bold - ie with two asterisks
#  either side of them

def make_all_words_bold(str_list):
    pass


@pytest.mark.skip()
def test_make_all_words_bold():
    assert make_all_words_bold(["hello", "there", "world"]) == [
        "**hello**", "**there**", "**world**"]
    assert make_all_words_bold(["I", "love", "coding"]) == [
        "**I**", "**love**", "**coding**"]


# QUESTION 7
# This function should take an list of numbers as an argument and return an
#  list containing all positive numbers from the input (retaining the order)
def get_positive_numbers(num_list):
    pass


@pytest.mark.skip()
def test_get_positive_numbers(num_list):
    assert get_positive_numbers([1, -1, 2, -2, 3, -3]) == [1, 2, 3]
    assert get_positive_numbers([-80, 9, 100, 13, 20, -7]) == [9, 100, 13, 20]
    assert get_positive_numbers([-1, -50, -999]) == []
