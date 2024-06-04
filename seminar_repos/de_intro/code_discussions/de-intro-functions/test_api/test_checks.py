from checks import (
    run_test, skip_test, format_err_msg,
    BOLD_GREEN, NORMAL_GREEN, BOLD_RED, NORMAL_RED, BOLD_YELLOW, NORMAL_YELLOW,
    DEFAULT
)
from unittest.mock import patch, call, Mock
import pytest


class TestRunTestDecorator:
    def test_wraps_function_correctly(self):
        def func_to_test():
            return 'hello'

        assert callable(run_test(func_to_test))

    def test_run_test_decorator_prints_success_message_if_tests_are_passing(self, capsys):
        @run_test
        def func_to_test():
            assert True

        func_to_test()

        captured = capsys.readouterr()

        expected_feedback = (f"{BOLD_GREEN}func_to_test()"
                             f"{NORMAL_GREEN}: Test passed ✅{DEFAULT}")

        assert expected_feedback in captured.out

    @patch('checks.print')
    def test_run_test_decorator_prints_failure_message_if_assert_fails(self, mock_print):
        def function_under_test():
            return True

        @run_test
        def testing_function():
            assert function_under_test() is False

        with pytest.raises(AssertionError) as e:
            testing_function()

        feedback_msg = (f"{BOLD_RED}testing_function(){NORMAL_RED}: "
                        f"Test failed ❌, see error message below:{DEFAULT}\n")
        expected_calls = [call(feedback_msg)]

        assert mock_print.mock_calls == expected_calls

    @patch('checks.print')
    def test_run_test_decorator_prints_failure_message_if_other_exception_raised(self, mock_print):
        function_under_test = Mock(side_effect=TypeError)

        @run_test
        def testing_function():
            assert function_under_test() is True

        with pytest.raises(TypeError) as e:
            testing_function()

        feedback_msg = (f"{BOLD_RED}testing_function(){NORMAL_RED}: "
                        f"Test failed ❌, see error message below:{DEFAULT}\n")
        expected_calls = [call(feedback_msg)]

        assert mock_print.mock_calls == expected_calls


class TestSkipTestDecorator:
    def test_wraps_function_correctly(self):
        def func_to_test():
            return 'hello'

        assert callable(skip_test(func_to_test))

    def test_skip_test_decorator_prints_skip_message(self, capsys):
        invocation_counter = 0

        def function_under_test():
            return True

        @skip_test
        def func_to_test():
            nonlocal invocation_counter
            invocation_counter += 1
            assert function_under_test() is True

        func_to_test()

        captured = capsys.readouterr()

        expected_feedback = (f"{BOLD_YELLOW}func_to_test()"
                             f"{NORMAL_YELLOW}: Test skipped 🔇{DEFAULT}")

        assert expected_feedback in captured.out
        assert invocation_counter == 0


class TestFormatErrorMessage:
    def test_format_error_message_returns_formatted_error_string(self):
        test_expected = 1
        test_received = 2

        expected_err_msg = (
            f"{NORMAL_RED}expected {test_expected}, instead received "
            f"{test_received}{DEFAULT}"
        )

        assert format_err_msg(test_expected, test_received) == expected_err_msg
