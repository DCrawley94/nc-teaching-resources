import pytest

# This function that takes an list of triangles.
# Each triangle is represented as an list e.g. [10, 12, 22] where the three
#  numbers are the sides of the triangle.
# The function should return the count of triangles that are valid.
# To be a valid triangle, the sum of any two sides must be larger than the
#  remaining side


def valid_triangles(triangles):
    pass


def test_valid_triangles_returns_0_when_passed_no_triangles():
    assert valid_triangles([]) == 0


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_valid_triangles_returns_0_when_passed_a_list_with_no_valid_triangles():
    assert valid_triangles([[5, 10, 25]]) == 0


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_valid_triangles_returns_1_when_passed_a_list_with_a_single_valid_triangle():
    assert valid_triangles([[5, 4, 5]]) == 1


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_valid_triangles_returns_1_when_passed_a_list_with_a_single_valid_triangle():
    assert valid_triangles([[5, 4, 5]]) == 1


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_valid_triangles_returns_2_when_passed_a_list_with_2_valid_and_1_invalid_triangle():
    assert valid_triangles([[5, 10, 25], [5, 4, 5], [542, 586, 419]]) == 2
