from src.example_2_difficult import run_and_log
from unittest.mock import patch


class TestDTStrfTime:
    def strftime(self, *args):
        return "2024-11-04 14:06:00"


def test_log_message_func_with_return_value():
    with patch("src.example_2_difficult.datetime") as patched_dt:
        patched_dt.now.return_value = TestDTStrfTime()

        # patched dt > has a now method
        # now method return object with strftime method - "2024-11-04 14:06:00"
        def func_with_return():
            return "test func response"

        assert run_and_log(func_with_return) == (
            "2024-11-04 14:06:00 - func_with_return ran successfully: test func response"
        )


@patch("src.example_2_difficult.datetime")
def test_log_message_function_exception(patched_dt):
    patched_dt.now().strftime.return_value = "2024-11-04 14:06:00"

    def func_that_raises_an_error():
        raise Exception("error message")

    assert run_and_log(func_that_raises_an_error) == (
        "2024-11-04 14:06:00 - func_that_raises_an_error encountered an error: error message"
    )
