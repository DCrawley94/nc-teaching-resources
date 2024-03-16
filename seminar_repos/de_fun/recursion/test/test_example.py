from src.example import count_ice_creams


def test_non_nested_list_no_ice_cream():
    assert count_ice_creams(["not ice cream"]) == 0


def test_non_nested_list_single_ice_cream():
    assert count_ice_creams(["ice cream"]) == 1


def test_non_nested_list_multiple_ice_creams():
    some_ice_creams = ["ice cream", "banana", "ice cream", "apple"]
    assert count_ice_creams(some_ice_creams) == 2


def test_nested_list_single_ice_cream():
    nested_ice_cream = [[["ice cream"]]]
    assert count_ice_creams(nested_ice_cream) == 1


def test_multiple_nested_items_varied_nesting():
    varied_nesting_search = [
        ["ice cream"],
        "sadness",
        [["ice cream"], "sadness"],
        [[["ice cream", "sadness"], "ice cream"]],
    ]

    assert count_ice_creams(varied_nesting_search) == 4
