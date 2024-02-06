from src.example_1 import process_data
from unittest.mock import patch


def test_process_data_1():
    patcher = patch('src.example_1.load_data', return_value=8)

    patcher.start()
    assert process_data() == 15
    patcher.stop()
