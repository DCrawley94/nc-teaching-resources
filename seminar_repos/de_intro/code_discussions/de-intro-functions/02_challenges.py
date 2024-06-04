from test_api.checks import run_test, skip_test, format_err_msg


# Challenge 6
# This function should take a string as an argument representing a file path
# and return True if it is an absolute path, and False otherwise.
# HINT: all absolute file paths start with a /


def is_absolute_path():
    pass


@run_test
def test_is_absolute_path():
    assert is_absolute_path("/Users/mitch") is True, \
        format_err_msg(True, is_absolute_path("/Users/mitch"))

    assert is_absolute_path(
        "/Users/mitch/northcoders/remote_course/remote_precourse_1"
    ) is True, \
        format_err_msg(True,  is_absolute_path(
            "/Users/mitch/northcoders/remote_course/remote_precourse_1"
        )
    )

    assert is_absolute_path("../composers") is False, \
        format_err_msg(False, is_absolute_path("../composers"))

    assert is_absolute_path("./applications/my-awesome-app.js") is False, \
        format_err_msg(False, is_absolute_path(
            "./applications/my-awesome-app.js"))


if __name__ == "__main__":
    test_is_absolute_path()
