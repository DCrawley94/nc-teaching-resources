from test_api.checks import run_test, skip_test, format_err_msg

# Fix the function below to pass the test!


def shopping_trip(money, item):
    items_and_prices = {
        "Danika's tears": 10,
        "Alex's soul": 3,
        "Simon's beard": 67,
        "Kyle's house": 49,
        "Chon's glasses": 23
    }
    if money <= items_and_prices[item]:
        return f"You can buy {item}!"

    return f"You can't afford {item}..."


@run_test
def test_returns_message_enough_money():
    expected_1 = "You can buy Danika's tears!"
    result_1 = shopping_trip(50, "Danika's tears")
    assert result_1 == expected_1, format_err_msg(expected_1, result_1)

    expected_2 = "You can buy Kyle's house!"
    result_2 = shopping_trip(50, "Kyle's house")
    assert result_2 == expected_2, format_err_msg(expected_2, result_2)


@skip_test
def test_returns_message_not_enough_money():
    expected = "You can't afford Simon's beard..."
    result = shopping_trip(50, "Simon's beard")
    assert result == expected, format_err_msg(expected, result)


if __name__ == '__main__':
    test_returns_message_enough_money()
    test_returns_message_not_enough_money()
