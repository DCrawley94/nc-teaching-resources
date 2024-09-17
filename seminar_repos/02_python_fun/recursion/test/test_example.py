from src.example import count_ice_creams


def test_count_ice_cream_returns_0_when_passed_empty_list():
    assert count_ice_creams([]) == 0


def test_count_ice_cream_non_nested_no_ice_cream():
    assert count_ice_creams(["not ice cream", "not ice cream", "not ice cream"]) == 0


def test_count_ice_cream_non_nested_with_ice_cream():
    assert count_ice_creams(["ice cream"]) == 1
    assert count_ice_creams(["ice cream", "ice cream"]) == 2


# nested list - returns count including nested "ice cream"
#   - doesn't contain ice cream
#   - contains ice cream


def test_count_ice_creams_nested_lists_without_ice_cream():
    nested_list = ["ice cream", ["not ice cream"], "ice cream"]
    assert count_ice_creams(nested_list) == 2


def test_count_ice_creams_nested_lists_with_ice_cream():
    nested_list = ["ice cream", ["ice cream"], "ice cream"]
    assert count_ice_creams(nested_list) == 3


def test_count_ice_creams_lots_of_nesting():
    varied_nesting_search = [
        ["ice cream"],
        "sadness",
        [["ice cream"], "sadness"],
        [[["ice cream", "sadness"], "ice cream"]],
    ]

    assert count_ice_creams(varied_nesting_search) == 4
