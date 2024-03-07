from src.extension.extension_bug_3 import capital_authors
import pytest


@pytest.mark.skip()
def test_returns_an_empty_list_when_passed_one():
    expected = []
    result = capital_authors([])
    assert result == expected


@pytest.mark.skip()
def test_returns_a_list_with_one_author_capitalised():
    expected = ["DANIKA"]
    result = capital_authors(["Danika - BASH your way out of any problem"])
    assert result == expected


@pytest.mark.skip()
def test_returns_list_of_capitalised_authors():
    expected = ['JOE', "PAUL", "SIMON"]
    result = capital_authors([
        "Joe - Data: Now I own you",
        "Paul - How I become a god",
        "Simon - Why rocks are wicked super cool"
    ])
    assert result == expected
