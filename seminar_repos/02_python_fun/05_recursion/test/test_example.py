from src.example import count_ice_creams


# empty list/no ice creams (no recursion) > 0
def test_non_nested_list_no_ice_cream():
    food_list = []
    assert count_ice_creams(food_list) == 0

    food_list = ["not ice cream", "banana"]
    assert count_ice_creams(food_list) == 0


# flat list (no recursion) containing ice cream
def test_non_nested_list_with_ice_cream():
    food_list = ["ice cream", "banana", "ice cream"]
    assert count_ice_creams(food_list) == 2


# test nested list with ice cream
def test_single_nested_list_with_ice_cream():
    food_list = ["banana", ["ice cream"]]
    assert count_ice_creams(food_list) == 1


# test multi levels of nesting
def test_multi_nested_list_with_ice_cream():
    food_list = ["banana", [["ice cream"]]]
    assert count_ice_creams(food_list) == 1


def test_nested_ice_creams_extended_list():
    food_list = ["banana", ["ice cream"], ["ice cream"]]
    assert count_ice_creams(food_list) == 2
