from test_api.checks import run_test, format_err_msg


# Fix the function below to pass the test!

def finding_Nemo(fish):
    fish_tank = {
        "Clown fish": "Nemo",
        "Blue Tang": "Dory",
        "Great White Shark": "Bruce",
        "Moorish Idol": "Gill",
        "Sea Turtle": "Crush"
    }
    return tank[fish]


@run_test
def test_returns_Nemo():
    expected = "Nemo"
    result = finding_Nemo("Clown fish")
    assert result == expected, format_err_msg(expected, result)


if __name__ == '__main__':
    test_returns_Nemo()
