from test_api.checks import run_test, format_err_msg


# Fix the function below to pass the test!

def multiply_by_3():
    return number * 3


@run_test
def test_returns_expected_number():
    assert multiply_by_3(1) == 3, format_err_msg(3, multiply_by_3(1))
    assert multiply_by_3(2) == 6, format_err_msg(6, multiply_by_3(2))
    assert multiply_by_3(3) == 9, format_err_msg(9, multiply_by_3(3))
    assert multiply_by_3(4) == 12, format_err_msg(12, multiply_by_3(4))


if __name__ == '__main__':
    test_returns_expected_number()
