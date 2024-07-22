from src.example_2 import get_games
from unittest.mock import patch

class MockConnection:
    def run(self, query):
        return []

@patch("src.example_2.Connection", return_value=MockConnection())
def test_no_games_no_data(mock_conn):
    assert get_games() == []

@patch("src.example_2.Connection")
def test_single_game(mock_conn):
    mock_conn_obj = mock_conn.return_value
    mock_conn_obj.run.return_value = [
        [1, 'Skyrim 2', 1999, 'www.website.com', 'PS2']]

    assert get_games() == [ 
        {
            'games_id': 1,
            'game_title': 'Skyrim 2',
            'release_year': 1999,
            'image_url': 'www.website.com',
            'console_name': 'PS2'
        }
    ]