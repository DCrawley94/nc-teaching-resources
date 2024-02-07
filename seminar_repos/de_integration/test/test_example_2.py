from src.example_2 import get_games
from unittest.mock import patch


# class MockConnection:
#     def run(self, query):
#         return []


def test_get_games_no_data():
    with patch('src.example_2.Connection') as mock_conn:
        mock_conn().run.return_value = []
        assert get_games() == []


def test_get_games_single_row():
    with patch('src.example_2.Connection') as mock_conn:
        mock_conn().run.return_value = [
            [1, 'game', 1999, 'www.website.com', 'PS2']
        ]

        assert get_games() == [
            {
                'games_id': 1,
                'game_title': 'game',
                'release_year': 1999,
                'image_url': 'www.website.com',
                'console_name': 'PS2'
            }
        ]
