import pytest


# Challenge 6
# This function should take a string as an argument representing a file path
# and return True if it is an absolute path, and False otherwise.
# HINT: all absolute file paths start with a /


def is_absolute_path():
    pass


@pytest.mark.skip()
def test_is_absolute_path():
    assert is_absolute_path("/Users/mitch") == True
    assert (
        is_absolute_path(
            "/Users/mitch/northcoders/remote_course/remote_precourse_1")
        == True
    )
    assert is_absolute_path("../composers") == False
    assert is_absolute_path("./applications/my-awesome-app.js") == False
