from test_api.checks import run_test, format_err_msg


# Fix the function below to pass the test!

def return_mentor_string(mentor):
    return f"Hello {Mentor}!"


@run_test
def test_returns_greeting():
    expected_1 = "Hello Alex!"
    result_1 = return_mentor_string("Alex")
    assert result_1 == expected_1, format_err_msg(expected_1, result_1)

    expected_2 = "Hello Danika!"
    result_2 = return_mentor_string("Danika")
    assert result_2 == expected_2, format_err_msg(expected_2, result_2)


if __name__ == '__main__':
    test_returns_greeting()
