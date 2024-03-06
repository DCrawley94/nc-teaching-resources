import pytest

# Implement a function collect_like_terms which takes an expression in a
#  string like 'a + a + a' and then returns a string with a simplified
#  algebraic expression, which in the previous case would be 3a.
# The characters should be in alphabetical order by default.
# You can assume that the only operation connecting the terms is addition.


def collect_like_terms():
    pass


def test_collect_like_terms_returns_a_letter_when_passed_an_expression_with_a_single_letter():
    assert collect_like_terms("a") == "a"
    assert collect_like_terms("b") == "b"


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_collect_like_terms_returns_the_expression_if_it_is_already_simplified_and_not_starting_with_a_1():
    assert collect_like_terms("2a") == "2a"
    assert collect_like_terms("3a") == "3a"


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_collect_like_terms_returns_just_the_letter_if_it_starts_with_a_1():
    assert collect_like_terms("1a") == "a"
    assert collect_like_terms("1y") == "y"


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_collect_like_terms_can_simplify_two_duplicated_letters_added_together():
    assert collect_like_terms("a + a") == "2a"
    assert collect_like_terms("c + c") == "2c"


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_collect_like_terms_can_simplify_multiple_duplicated_letters_added_together():
    assert collect_like_terms("a + a + a") == "3a"
    assert collect_like_terms("z + z + z + z") == "4z"


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_collect_like_terms_can_simplify_two_distinct_letters_in_alphabetical_order():
    assert collect_like_terms("a + b") == "a + b"
    assert collect_like_terms("b + a") == "a + b"


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_collect_like_terms_can_simplify_a_mix_of_distinct_and_duplicate_letters_being_added_together():
    assert collect_like_terms("a + b + b") == "a + 2b"
    assert collect_like_terms("a + a + a + b") == "3a + b"


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_collect_like_terms_can_simplify_multiple_distinct_terms():
    assert collect_like_terms("ab + ab") == "2ab"
    assert collect_like_terms("ab + ab + ab") == "3ab"
