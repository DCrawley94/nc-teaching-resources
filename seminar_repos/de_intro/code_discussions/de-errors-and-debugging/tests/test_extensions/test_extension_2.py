from src.extension.extension_bug_2 import clever_banking
import pytest


@pytest.mark.skip()
def test_returns_same_value_when_interest_is_zero_for_5_years():
    expected = 100
    result = clever_banking(100, 0, 5)
    assert result == expected


@pytest.mark.skip()
def test_returns_same_value_when_years_are_0():
    expected = 100
    result = clever_banking(100, 3.2, 0)
    assert result == expected


@pytest.mark.skip()
def test_returns_correct_when_interest_rates_and_years_are_greater_than_0():
    expected = 161.05
    result = clever_banking(100, 0.1, 5)
    assert result == expected
