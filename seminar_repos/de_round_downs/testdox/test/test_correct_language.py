from src.correct_language import correct_language
import pytest


def test_correct_language_returns_a_new_list():
    # arrange
    input1 = [
        {"name": "Kyle", "language": "Javascript"},
        {"name": "Liam", "language": "Go"}
    ]
    # act
    result = correct_language(input1)

    # assert
    assert result is not input1


def test_correct_language_does_not_mutate_input():
    # arrange
    input1 = [
        {"name": "Kyle", "language": "Javascript"},
        {"name": "Liam", "language": "Go"}
    ]
    expected_input = [
        {"name": "Kyle", "language": "Javascript"},
        {"name": "Liam", "language": "Go"}
    ]
    # act
    correct_language(input1)

    # assert
    assert input1 == expected_input


def test_correct_language_does_not_change_profiles_when_language_is_python():
    # arrange
    input1 = [{"name": "Kyle", "language": "Python"}]
    expected = [{"name": "Kyle", "language": "Python"}]
    # act
    result = correct_language(input1)

    # assert
    assert result == expected


def test_changes_language_of_single_non_Python_profile():
    # arrange
    input1 = [{"name": "Liam", "language": "Javascript"}]
    expected = [{"name": "Liam", "language": "Python"}]
    # act
    result = correct_language(input1)

    # assert
    assert result == expected


def test_changes_language_of_multiple_non_Python_profiles():
    # arrange
    input1 = [
        {"name": "Kyle", "language": "Javascript"},
        {"name": "Liam", "language": "Go"}
    ]
    expected = [
        {"name": "Kyle", "language": "Python"},
        {"name": "Liam", "language": "Python"}
    ]
    # act
    result = correct_language(input1)

    # assert
    assert result == expected