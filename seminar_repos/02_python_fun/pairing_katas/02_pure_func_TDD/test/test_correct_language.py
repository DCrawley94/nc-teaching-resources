from src.correct_language import correct_language
import pytest


@pytest.mark.it("when passed an empty list, function should return an empty list")
def test_correct_language_returns_empty_list_when_passed_empty_list():
    input_list = []
    expected_output = []

    result = correct_language(input_list)

    assert result == expected_output


def test_correct_language_should_return_a_new_list():
    input_list = []

    result = correct_language(input_list)

    assert result is not input_list


def test_correct_language_single_profile_no_change_needed():
    input_list = [{"name": "Kyle", "language": "Python"}]
    expected_output = [{"name": "Kyle", "language": "Python"}]

    result = correct_language(input_list)

    assert result == expected_output


def test_correct_language_single_profile_not_python():
    input_list = [{"name": "Kyle", "language": "JavaScript"}]
    expected_output = [{"name": "Kyle", "language": "Python"}]

    result = correct_language(input_list)

    assert result == expected_output


def test_correct_language_avoids_mutating_the_input():
    input_list = [{"name": "Kyle", "language": "JavaScript"}]

    correct_language(input_list)

    assert input_list == [{"name": "Kyle", "language": "JavaScript"}]
