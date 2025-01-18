from db.seed import create_game_lookup


# [[1, 'Mario Kart 64'], [2, 'Donkey Kong'], [3, 'Mario Bros']]
# {'mario kart'; : 1, ....}


def test_create_game_lookup_single_row():
    input_rows = [[1, "Mario Kart 64"]]
    expected = {"Mario Kart 64": 1}

    result = create_game_lookup(input_rows)

    assert result == expected


def test_create_game_lookup_multi_rows():
    input_rows = [[1, "Mario Kart 64"], [2, "Donkey Kong"], [3, "Mario Bros"]]
    expected = {"Mario Kart 64": 1, "Donkey Kong": 2, "Mario Bros": 3}

    result = create_game_lookup(input_rows)

    assert result == expected
