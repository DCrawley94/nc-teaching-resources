from test_api.checks import run_test, format_err_msg


# Fix the function below to pass the test!

def access_dictionary(mentor):
    favourite_show = {
        "Alex": "Spelling with cbeebies",
        "Danika": "The Simpsons",
        "Simon": "My Little Pony",
        "Kyle": "Battlestar galactica",
        "Chon": "Rick and Morty"
    }
    return favourite_show.mentor


@run_test
def test_accesses_correct_value():
    expected_1 = "Spelling with cbeebies"
    result_1 = access_dictionary("Alex")
    assert result_1 == expected_1, format_err_msg(expected_1, result_1)

    expected_2 = "The Simpsons"
    result_2 = access_dictionary("Danika")
    assert result_2 == expected_2, format_err_msg(expected_2, result_2)

    expected_3 = "My Little Pony"
    result_3 = access_dictionary("Simon")
    assert result_3 == expected_3, format_err_msg(expected_3, result_3)

    expected_4 = "Battlestar galactica"
    result_4 = access_dictionary("Kyle")
    assert result_4 == expected_4, format_err_msg(expected_4, result_4)

    expected_5 = "Rick and Morty"
    result_5 = access_dictionary("Chon")
    assert result_5 == expected_5, format_err_msg(expected_5, result_5)


if __name__ == '__main__':
    test_accesses_correct_value()
