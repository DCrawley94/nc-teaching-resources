import pytest

# This function marks passwords out of 7 using the scores below.
# Invalid inputs should return 0.

# Score	Criteria	Example
# 1: Less than four characters	e.g. bob
# 2: Less than nine characters	e.g. bobbybob
# 3: More than eight characters and all letters	e.g. bobbobbob
# 4: More than eight characters includes a number	e.g. bobbobbob1
# 5: More than eight characters includes a number and special character
#  e.g. bobbob1#2$
# 6: More than twelve characters includes a number	e.g. bobbobbobbob123
# 7: More than twelve characters includes a number and special character
#  e.g. bobbobbob1!2@3#

# Special characters: ! @ £ # $ % ^ & *


def password_score(password):
    pass


def test_password_score_returns_score_1_for_less_than_four_characters():
    assert password_score("cat") == 1


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_password_score_returns_score_2_for_less_than_nine_characters():
    assert password_score("cattycat") == 2


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_password_score_returns_score_3_for_more_than_eight_characters():
    assert password_score("catcatcat") == 3


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_password_score_returns_score_4_for_more_than_eight_characters_and_includes_a_number():
    assert password_score("catcatcat1") == 4


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_password_score_returns_score_5_for_more_than_eight_characters_which_includes_a_number_and_special_character():
    assert password_score("catcat1#2$") == 5


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_password_score_returns_score_6_for_more_than_twelve_characters_which_includes_a_number():
    assert password_score("catcatcatcat123") == 6


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_password_score_returns_score_7_for_more_than_twelve_characters_which_includes_a_number_and_special_character():
    assert password_score("catcatcat1!2@3#") == 7
