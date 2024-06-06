from test_api.checks import run_test, format_err_msg


#  Fix the function below to pass the test!

def say_hello():
    return "Hello Dat Engineers."


@run_test
def test_returns_correct_value():
    expected = 'Hello Data Engineers.'
    result = say_hello()
    assert result == expected, format_err_msg(expected, result)


if __name__ == '__main__':
    test_returns_correct_value()
