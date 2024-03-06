import pytest

# Implement a function which takes any decimal number and converts it into
#  binary format.
# The return value of the function should always be a string of "O"s and
#  "1"s representing the binary number


def convert_to_binary():
    pass


def test_convert_to_binary_can_convert_a_single_digit_decimal_number_to_binary():
    assert convert_to_binary(0) == "0"
    assert convert_to_binary(1) == "1"
    assert convert_to_binary(2) == "10"
    assert convert_to_binary(3) == "11"
    assert convert_to_binary(4) == "100"
    assert convert_to_binary(5) == "101"
    assert convert_to_binary(6) == "110"
    assert convert_to_binary(7) == "111"


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_convert_to_binary_can_convert_a_multiple_digit_decimal_number_to_binary():
    assert convert_to_binary(10) == "1010"
    assert convert_to_binary(23) == "10111"
    assert convert_to_binary(55) == "110111"
