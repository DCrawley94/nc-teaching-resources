from test_api.checks import run_test, skip_test, format_err_msg


# Fix the function below to pass the tests!

def capital_authors(list):
    authors = []

    for pair in list:
        authors.append(pair.split("-"))

    return authors


@run_test
def test_returns_an_empty_list_when_passed_one():
    expected = []
    result = capital_authors([])
    assert result == expected, format_err_msg(expected, result)


@run_test
def test_returns_a_list_with_one_author_capitalised():
    expected = ["DANIKA"]
    result = capital_authors(["Danika - BASH your way out of any problem"])
    assert result == expected, format_err_msg(expected, result)


@skip_test
def test_returns_list_of_capitalised_authors():
    expected = ['JOE', "PAUL", "SIMON"]
    result = capital_authors([
        "Joe - Data: Now I own you",
        "Paul - How I become a god",
        "Simon - Why rocks are wicked super cool"
    ])
    assert result == expected, format_err_msg(expected, result)


if __name__ == '__main__':
    test_returns_an_empty_list_when_passed_one()
    test_returns_a_list_with_one_author_capitalised()
    test_returns_list_of_capitalised_authors()
