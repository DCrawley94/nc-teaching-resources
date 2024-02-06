from src.example_2 import get_games
from unittest.mock import patch


@patch('src.example_2.Connection')
def test_get_games_no_data(mock_conn):
    mock_conn().run.return_value = []
    # I can leverage the functionality of the `mock`
    # This is essentially saying that the return value of
    # Connection will be a Mock and that Mock will have a `run` method`
    assert get_games() == []
