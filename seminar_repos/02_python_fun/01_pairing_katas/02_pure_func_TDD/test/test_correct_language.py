from src.correct_language import correct_language


def test_correct_language_given_empty_list_returns_empty_list():
    input_list = []
    expected_value = []

    result = correct_language(input_list)

    assert result == expected_value


def test_correct_language_no_change_to_python_language():
    input_list = [{"name": "Kyle", "language": "Python"}]
    expected_value = [{"name": "Kyle", "language": "Python"}]

    result = correct_language(input_list)

    assert result == expected_value


def test_changes_language_for_single_profile():
    input_list = [{"name": "Kyle", "language": "Java"}]
    expected_value = [{"name": "Kyle", "language": "Python"}]

    result = correct_language(input_list)

    assert result == expected_value


def test_changes_language_for_multiple_profiles():
    input_list = [
        {"name": "Kyle", "language": "Javascript"},
        {"name": "Liam", "language": "Go"},
    ]
    expected_value = [
        {"name": "Kyle", "language": "Python"},
        {"name": "Liam", "language": "Python"},
    ]

    result = correct_language(input_list)
    assert result == expected_value


def test_correct_language_should_not_mutate_input():
    input_list = [
        {"name": "Kyle", "language": "Javascript"},
        {"name": "Liam", "language": "Go"},
    ]

    correct_language(input_list)

    assert input_list == [
        {"name": "Kyle", "language": "Javascript"},
        {"name": "Liam", "language": "Go"},
    ]


def test_correct_language_return_new_list():
    input_list = [
        {"name": "Kyle", "language": "Javascript"},
        {"name": "Liam", "language": "Go"},
    ]
    result = correct_language(input_list)

    assert result is not input_list
