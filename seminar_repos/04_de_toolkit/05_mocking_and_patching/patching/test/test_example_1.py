from src.example_1 import process_data
from unittest.mock import patch


def test_process_data_manual_patch():
    patcher = patch("src.example_1.load_data", return_value=8)

    patcher.start()
    assert process_data() == "The processed data is 15"
    patcher.stop()


def test_process_data_context_manager_patch():
    with patch("src.example_1.load_data") as patched_load_data:
        patched_load_data.return_value = 8
        assert process_data() == "The processed data is 15"


@patch("src.example_1.load_data")
def test_process_data_decorator_patch(patched_load_data):
    patched_load_data.return_value = 8

    assert process_data() == "The processed data is 15"
