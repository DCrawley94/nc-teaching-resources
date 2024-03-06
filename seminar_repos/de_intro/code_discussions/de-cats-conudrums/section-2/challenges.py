import pytest


# QUESTION 1
# This function should take two strings as arguments and return True if
#  their final character is the same or False if not

def check_same_final_character():
    pass


def test_check_same_final_character():
    assert check_same_final_character("hello", "hello") == True
    assert check_same_final_character("goodbye!", "goodbye?") == False
    assert check_same_final_character("north", "coders") == False
    assert check_same_final_character("what", "did you expect") == True


# QUESTION 2
# This function should take a string as an argument and return True if
#  every letter is upper case and False if at least one character is not

def is_all_upper_case():
    pass


@pytest.mark.skip()
def test_is_all_upper_case():
    assert is_all_upper_case("hello") == False
    assert is_all_upper_case("WORLD") == True
    assert is_all_upper_case("HI Mabel") == False
    assert is_all_upper_case("NORTHCODERS WHOO") == True


# QUESTION 3
# This function should take a string as its argument and return a
#  string consisting of all vowels found in the input (retaining the order)

def collect_the_vowels(str):
    pass


@pytest.mark.skip()
def test_collect_the_vowels():
    assert collect_the_vowels("a") == "a"
    assert collect_the_vowels("bcd") == ""
    assert collect_the_vowels("bcdepiaouk") == "eiaou"
    assert collect_the_vowels("hello world") == "eoo"


# QUESTION 4
# This function should take two arguments, an list and an index, and return
#  the element at that specified index

# The index provided may be equal to or greater than the length of the
#  given list. In this case, rather than counting past the end of the
#  list where there are no values, the indexing should be considered to
#  "loop back around" and continue from the start of the list

# For examples of this behaviour, look at the second group of tests below

def access_item(list, index):
    pass


@pytest.mark.skip()
def test_access_item_retrieves_item_when_passed_index_less_than_list_len():
    assert access_item(["a", "b", "c", "d"], 2) == "c"
    assert access_item(["a", "b", "c", "d"], 0) == "a"
    assert access_item(["a", "b", "c", "d"], 3) == "d"


@pytest.mark.skip()
def test_access_item_retrieves_item_when_passed_index_greater_or_equal_to_list_len():
    assert access_item(["a", "b", "c", "d"], 4) == "a"
    assert access_item(["a", "b", "c", "d"], 6) == "c"
    assert access_item(["a", "b", "c", "d"], 10) == "c"


# QUESTION 5
# This function should take a number from 1 to 7 inclusive, and return a
#  string of the corresponding day of the week
# BONUS POINTS: Try and solve this without using if statements! Hint: a
#  'lookup dictionary' might be useful here.

def find_day_of_the_week(num):
    pass


@pytest.mark.skip()
def test_find_day_of_the_week():
    assert find_day_of_the_week(3) == "Wednesday"
    assert find_day_of_the_week(7) == "Sunday"
    assert find_day_of_the_week(1) == "Monday"


# QUESTION 6
# This function should take two numbers, a and b, and return a string
#  representing the value of a as a percentage of b

def create_percentage():
    pass


@pytest.mark.skip()
def test_create_percentage():
    assert create_percentage(1, 2) == "50%"
    assert create_percentage(50, 100) == "50%"
    assert create_percentage(2, 3) == "67%"
    assert create_percentage(3, 4) == "75%"
    assert create_percentage(1, 7) == "14%"


# QUESTION 7
# This function should take a string containing a number wrapped in a pair
#  of round brackets and return said number

def extract_number():
    pass


@pytest.mark.skip()
def test_extract_number():
    assert extract_number("lasjdasasj(1)asljdlajk") == 1
    assert extract_number("qwasdaoyer(666)iuwyeibasdahgsd") == 666
    assert extract_number("qwasdasdfsyer(19827)iusdfsdfsd") == 19827
    assert extract_number("qwasdasdfsyer(5601)iusd5602sdfsd") == 5601
    assert extract_number("qwasdas27dfs28yer(29)ius3dfsdf0sd") == 29
