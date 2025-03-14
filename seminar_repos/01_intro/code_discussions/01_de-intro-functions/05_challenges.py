from test_api.checks import run_test, skip_test, format_err_msg

# If we list all the whole numbers below 10 that are multiples of 3 or 5, we
#  get 3, 5, 6 and 9.
# The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3
#  or 5 below the limit passed in as an argument.
# Additionally, if the number is negative, return 0.

# Note: If the number is a multiple of both 3 and 5, only count it once!


def find_total_of_multiples(limit):
    pass


@skip_test
def test_find_total_of_multiples():
    # find_total_of_multiples() return zero for negative numbers
    assert find_total_of_multiples(-1) == 0, format_err_msg(
        0, find_total_of_multiples(-1)
    )

    # find_total_of_multiples() returns first multiple of 3
    assert find_total_of_multiples(4) == 3, format_err_msg(
        3, find_total_of_multiples(4)
    )

    # find_total_of_multiples() returns sum of multiples of 3 or 5  below limit

    assert find_total_of_multiples(6) == 8, format_err_msg(
        8, find_total_of_multiples(6)
    )

    assert find_total_of_multiples(10) == 23, format_err_msg(
        23, find_total_of_multiples(10)
    )


if __name__ == "__main__":
    test_find_total_of_multiples()
