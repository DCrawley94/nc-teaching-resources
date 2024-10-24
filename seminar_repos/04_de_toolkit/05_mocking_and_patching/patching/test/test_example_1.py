from src.example_1 import process_data
from unittest.mock import patch


def test_process_data_1():
    patcher = patch("src.example_1.load_data", return_value=8)

    patcher.start()
    assert process_data() == "The processed data is 15"
    patcher.stop()


def test_process_data_2():
    with patch("src.example_1.load_data", return_value=8):
        assert process_data() == "The processed data is 15"


@patch("src.example_1.load_data", return_value=8)
def test_process_data_3(patch_load_data):
    assert process_data() == "The processed data is 15"
