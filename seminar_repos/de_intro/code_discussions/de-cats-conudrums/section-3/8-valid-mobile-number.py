import pytest

# For this function take a look at what is expected in the tests to help you
#  determine what behaviour your function should exhibit

# declare valid_mobile_number function here:


def test_valid_mobile_number_returns_false_when_passed_a_string_of_the_wrong_length():
    assert valid_mobile_number('123') == False
    assert valid_mobile_number('0750617250638') == False
    assert valid_mobile_number('+447712368768724988') == False


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_valid_mobile_number_returns_true_when_passed_a_valid_plain_phone_num_string():
    assert valid_mobile_number('07506172506') == True


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_valid_mobile_number_returns_true_when_passed_a_valid_string_with_a_plus_prefix():
    assert valid_mobile_number('+447506172506') == True


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_valid_mobile_number_returns_true_when_passed_a_valid_international_phone_num():
    assert valid_mobile_number('00447506172506') == True


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_valid_mobile_number_returns_false_when_passed_a_string_with_invalid_chars():
    assert valid_mobile_number('07506189foo') == False


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_valid_mobile_number_returns_true_when_passed_random_valid_phone_nums():
    assert valid_mobile_number('00447555123456') == True
    assert valid_mobile_number('+447676111222') == True
    assert valid_mobile_number('07898888643') == True
    assert valid_mobile_number('07989765490') == True


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_valid_mobile_number_returns_false_when_passed_random_invalid_phone_nums():
    assert valid_mobile_number('004475551&&&23456') == False
    assert valid_mobile_number('-447676111222') == False
    assert valid_mobile_number('00448989765493') == False
    assert valid_mobile_number('cats') == False
