from db.utils import create_games_lookup, format_reviews

def test_create_games_lookup_empty_list():
    assert create_games_lookup([]) == {}

def test_create_games_lookup_single_game():
    test_games_input = [[1, 'Mario Kart 64', 1996, 'N64', 'test_url.jpg']]

    assert create_games_lookup(test_games_input) == {'Mario Kart 64': 1}

def test_create_games_lookup_multiple_games():
    test_games_input = [
        [1, 'Mario Kart 64', 1996, 'N64', 'test_url.jpg'],
        [2, 'Donkey Kong', 1983, 'NES', 'test_url.jpg'], 
        [3, 'Mario Bros', 1985, 'NES', 'test_url.jpg']
    ]
    assert create_games_lookup(test_games_input) == {'Mario Kart 64': 1, 'Donkey Kong': 2, 'Mario Bros': 3}


def test_format_reviews_empty_list():
    assert format_reviews([], {}) == []

def test_format_reviews_single_review():
    input_reviews = [
        {
            "username": "fola",
            "game_title": "Mario Kart 64",
            "comment": "Comment comment comment",
            "rating": 5
	    }
    ]
    input_lookup = {
        "Mario Kart 64": 1
    }

    expected = [
        {
            "username": "fola",
            "game_id": 1,
            "comment": "Comment comment comment",
            "rating": 5
	    }
    ]

    assert format_reviews(input_reviews, input_lookup) == expected

def test_format_reviews_multi_reviews():
    input_reviews = [
        {
            "username": "fola",
            "game_title": "Mario Kart 64",
            "comment": "Comment comment comment",
            "rating": 5
	    },
        {
            "username": "rogersop",
            "game_title": "Donkey Kong",
            "comment": "another comment",
            "rating": 4
	    }
    ]
    input_lookup = {
        "Mario Kart 64": 1,
        "Donkey Kong": 2
    }

    expected = [
        {
            "username": "fola",
            "game_id": 1,
            "comment": "Comment comment comment",
            "rating": 5
	    },
        {
            "username": "rogersop",
            "game_id": 2,
            "comment": "another comment",
            "rating": 4
	    }
    ]

    assert format_reviews(input_reviews, input_lookup) == expected