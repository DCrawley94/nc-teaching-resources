from src.extension.extension_bug_1 import confused_greeting
import pytest


@pytest.mark.skip()
def test_returns_empty_list_when_passed_empty_list():
    expected = []
    result = confused_greeting([])
    assert result == expected


@pytest.mark.skip()
def test_returns_list_with_one_name_appended_with_symbols():
    expected = ['Alex?!']
    result = confused_greeting(["Alex"])
    assert result == expected


@pytest.mark.skip()
def test_returns_list_of_names_with_symbols_appended():
    expected = ['Joe?!', 'Paul?!', 'Chon?!', 'Kyle?!']
    result = confused_greeting(['Joe', 'Paul', 'Chon', 'Kyle'])
    assert result == expected
