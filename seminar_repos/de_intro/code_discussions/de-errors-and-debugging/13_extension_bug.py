from test_api.checks import run_test, skip_test, format_err_msg


# Fix the function below to pass the tests!

def clever_banking(value, interest_rate, years):
    bank_account = value

    for i in range(1, years + 1):
        bank_account += (1 + interest_rate)

    return value


@run_test
def test_returns_same_value_when_interest_is_zero_for_5_years():
    expected = 100
    result = clever_banking(100, 0, 5)
    assert result == expected, format_err_msg(expected, result)


@skip_test
def test_returns_same_value_when_years_are_0():
    expected = 100
    result = clever_banking(100, 3.2, 0)
    assert result == expected, format_err_msg(expected, result)


@skip_test
def test_returns_correct_when_interest_rates_and_years_are_greater_than_0():
    expected = 161.05
    result = clever_banking(100, 0.1, 5)
    assert result == expected, format_err_msg(expected, result)


if __name__ == '__main__':
    test_returns_same_value_when_interest_is_zero_for_5_years()
    test_returns_same_value_when_years_are_0()
    test_returns_correct_when_interest_rates_and_years_are_greater_than_0()
