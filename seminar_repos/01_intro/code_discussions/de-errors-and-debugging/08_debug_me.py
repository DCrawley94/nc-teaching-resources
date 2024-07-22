from test_api.checks import run_test, format_err_msg


# Fix the function below to pass the test!

def return_last_digit(number):
    digit_string = str(number)
    return digit_string[-1]


@run_test
def test_returns_correct_number():
    expected_1 = 1
    result_1 = return_last_digit(1)
    assert result_1 == expected_1, format_err_msg(expected_1, result_1)

    expected_2 = 8
    result_2 = return_last_digit(28)
    assert result_2 == expected_2, format_err_msg(expected_2, result_2)

    expected_3 = 6
    result_3 = return_last_digit(456)
    assert result_3 == expected_3, format_err_msg(expected_3, result_3)

    expected_4 = 3
    result_4 = return_last_digit(7653)
    assert result_4 == expected_4, format_err_msg(expected_4, result_4)


if __name__ == '__main__':
    test_returns_correct_number()
