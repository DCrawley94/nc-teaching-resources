from test_api.checks import run_test, skip_test, format_err_msg


# Fix the function below to pass the tests!

def sum_sentence(list):
    costs = []
    for fruit_dict in list:
        costs.append(fruit_dict['cost'])

    total = costs

    return "The total cost of the fruits is £" + str(total)


@run_test
def test_returns_correct_string_when_passed_an_empty_list():
    expected = "The total cost of the fruits is £0"
    result = sum_sentence([])
    assert result == expected, format_err_msg(expected, result)


@skip_test
def test_returns_correct_string_for_one_fruit():
    expected = "The total cost of the fruits is £5"
    result = sum_sentence([{"fruit": "apple", "cost": 5}])
    assert result == expected, format_err_msg(expected, result)


@skip_test
def test_returns_correct_string_for_multiple_fruits():
    expected = "The total cost of the fruits is £33"
    result = sum_sentence([
        {"fruit": "red apple", "cost": 5},
        {"fruit": "poison apple", "cost": 20},
        {"fruit": "kiwi", "cost": 1},
        {"fruit": "tomato ;)", "cost": 2},
        {"fruit": "green apple", "cost": 5},
    ])
    assert result == expected, format_err_msg(expected, result)


if __name__ == '__main__':
    test_returns_correct_string_when_passed_an_empty_list()
    test_returns_correct_string_for_one_fruit()
    test_returns_correct_string_for_multiple_fruits()
