from test_api.checks import run_test, format_err_msg


# Fix the function below to pass the test!

def super_flyers(heroes):
    known_flying_heroes = []

    for hero in heroes:
        if hero["ability"] == "flying" or hero["isAnonymous"]:
            known_flying_heroes.append(hero)

    return known_flying_heroes


@run_test
def test_returns_correct_supers():
    heroes = [
        {
            "name": "Simonman",
            "ability": "Read rocks minds",
            "isAnonymous": True
        },
        {"name": "Kyleman", "ability": "flying", "isAnonymous": True},
        {"name": "Supercat", "ability": "flying", "isAnonymous": False},
        {
            "name": "DecoratorDani",
            "ability": "commercial painting",
            "isAnonymous": True
        },
        {"name": "LambdaChon", "ability": "flying", "isAnonymous": False},
        {
            "name": "SmartAlex",
            "ability": "reading and writing",
            "isAnonymous": True
        }
    ]
    expected = [
        {"name": "Supercat", "ability": "flying", "isAnonymous": False},
        {"name": "LambdaChon", "ability": "flying", "isAnonymous": False},
    ]
    result = super_flyers(heroes)
    assert result == expected, format_err_msg(expected, result)


if __name__ == '__main__':
    test_returns_correct_supers()
