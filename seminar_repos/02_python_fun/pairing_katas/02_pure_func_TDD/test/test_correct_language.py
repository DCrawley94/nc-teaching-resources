from src.correct_language import correct_language

def test_correct_language_returns_empty_list_when_passed_empty_list():
    test_list = []
    result = correct_language(test_list)

    assert result == []

def test_correct_language_returns_single_user_with_language_already_set_to_python():
    test_list = [{ "name" : "Kyle", "language" : "Python" }]

    expected_return = [{ "name" : "Kyle", "language" : "Python" }]

    result = correct_language(test_list)

    assert result == expected_return

def test_correct_language_returns_single_user_with_language_changed_to_python():
    test_list = [{ "name" : "Kyle", "language" : "Javascript" }]

    expected_return = [{ "name" : "Kyle", "language" : "Python" }]

    result = correct_language(test_list)

    assert result == expected_return

def test_correct_language_does_not_mutate_input():
    test_list = [{ "name" : "Kyle", "language" : "Javascript" }]

    correct_language(test_list)

    assert test_list == [{ "name" : "Kyle", "language" : "Javascript" }]

# check reference of return value
def test_correct_language_returns_new_reference_in_memory():
    test_list = [{ "name" : "Kyle", "language" : "Javascript" }]

    result = correct_language(test_list)

    assert result is not test_list
