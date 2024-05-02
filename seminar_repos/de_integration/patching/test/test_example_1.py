from src.example_1 import process_data
from unittest.mock import patch


def test_process_data_1():
    patcher = patch("src.example_1.load_data", return_value=8)

    patcher.start()
    assert process_data() == 'The processed data is 15'
    patcher.stop()


def test_process_data_2():
    with patch("src.example_1.load_data", return_value=8) as p:
        print(f"p: {p}")
        assert process_data() == 'The processed data is 15'


@patch("src.example_1.load_data")
def test_process_data_3(mock_load_data):
    mock_load_data.return_value = 8
    assert process_data() == 'The processed data is 15'
