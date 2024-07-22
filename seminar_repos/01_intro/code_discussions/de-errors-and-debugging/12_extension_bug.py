from test_api.checks import run_test, skip_test, format_err_msg


# Fix the function below to pass the tests!

def confused_greeting(names):

    confused_shouts = {}

    for name in names:
        confused_shouts.append(word + "? !")

    return confused_shoots


@run_test
def test_returns_empty_list_when_passed_empty_list():
    expected = []
    result = confused_greeting([])
    assert result == expected, format_err_msg(expected, result)


@skip_test
def test_returns_list_with_one_name_appended_with_symbols():
    expected = ['Alex?!']
    result = confused_greeting(["Alex"])
    assert result == expected, format_err_msg(expected, result)


@skip_test
def test_returns_list_of_names_with_symbols_appended():
    expected = ['Joe?!', 'Paul?!', 'Chon?!', 'Kyle?!']
    result = confused_greeting(['Joe', 'Paul', 'Chon', 'Kyle'])
    assert result == expected, format_err_msg(expected, result)


if __name__ == '__main__':
    test_returns_empty_list_when_passed_empty_list()
    test_returns_list_with_one_name_appended_with_symbols()
    test_returns_list_of_names_with_symbols_appended()
