from test_api.checks import run_test, format_err_msg


# Fix the function below to pass the test!

def add_numbers(num1, num2):
    return int(num1 + num2)


@run_test
def test_returns_correct_value():
    expected_1 = 4
    result_1 = add_numbers("2", "2")
    assert result_1 == expected_1, format_err_msg(expected_1, result_1)

    expected_2 = 10
    result_2 = add_numbers("5", "5")
    assert result_2 == expected_2, format_err_msg(expected_2, result_2)

    expected_3 = 1500
    result_3 = add_numbers("750", "750")
    assert result_3 == expected_3, format_err_msg(expected_3, result_3)


if __name__ == '__main__':
    test_returns_correct_value()
