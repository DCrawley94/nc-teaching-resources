from src.exercises.debug_me_11 import super_flyers
import pytest


@pytest.mark.skip()
def test_returns_correct_supers():
    heroes = [
        {
            "name": "Simonman",
            "ability": "Read rocks minds",
            "isAnonymous": True
        },
        {"name": "Kyleman", "ability": "flying", "isAnonymous": True},
        {"name": "Supercat", "ability": "flying", "isAnonymous": False},
        {
            "name": "DecoratorDani",
            "ability": "commercial painting",
            "isAnonymous": True
        },
        {"name": "LambdaChon", "ability": "flying", "isAnonymous": False},
        {
            "name": "SmartAlex",
            "ability": "reading and writing",
            "isAnonymous": True
        }
    ]
    expected = [
        {"name": "Supercat", "ability": "flying", "isAnonymous": False},
        {"name": "LambdaChon", "ability": "flying", "isAnonymous": False},
    ]
    result = super_flyers(heroes)
    assert result == expected
