from test_api.checks import run_test, format_err_msg


# Fix the function below to pass the test!

def return_dog_string():
    dog_name = "Mackrel"
    return f"Hello, I am a fancy talking dog and my name is {dog_name}."


@run_test
def test_returns_correct_value():
    expected = 'Hello, I am a fancy talking dog and my name is Mackerel.'
    result = return_dog_string()
    assert result == expected, format_err_msg(expected, result)


if __name__ == '__main__':
    test_returns_correct_value()
