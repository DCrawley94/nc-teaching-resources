import pytest

# This function folds a list in the middle n number of times.

# If the list has a odd length, then fold on the middle index (the
#  middle number therefore won't change)
# other wise you fold in the 'gap' between the two middle integers and so
#  all integers are folded.

# To 'fold' the numbers add them together.

# For example:

# Fold 1-times:
# [1,2,3,4,5] -> [6,6,3]
# Here we fold the 1st with the last and the second with the 4th. As it is
#  odd in length, the middle index is not folded


def fold_list():
    pass


def test_fold_list_folds_an_even_length_list():
    assert fold_list([1, 2], 1) == [3]
    assert fold_list([1, 2, 3, 10, 34, 100], 1) == [101, 36, 13]


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_fold_list_folds_an_odd_length_list():
    assert fold_list([1, 2, 3], 1) == [4, 2]


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_fold_list_folds_an_even_length_list_multiple_times():
    assert fold_list([1, 2, 3, 10, 34, 100], 2) == [114, 36]


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_fold_list_folds_a_list_to_a_single_value():
    assert fold_list([1, 2, 3, 10, 34, 100], 3) == [150]


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_fold_list_returns_repeated_folds_remain_the_same():
    assert fold_list([1, 2, 3, 10, 34, 100], 4) == [150]
