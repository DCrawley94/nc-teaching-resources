from src.exercises.debug_me_10 import finding_Nemo
import pytest


@pytest.mark.skip()
def test_returns_Nemo():
    expected = "Nemo"
    result = finding_Nemo("Clown fish")
    assert result == expected
