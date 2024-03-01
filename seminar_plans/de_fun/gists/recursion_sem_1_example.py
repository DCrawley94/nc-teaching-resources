"""
# count_ice_cream

create a function that accepts an array as an argument, this array will either 
contain strings or lists which can also contain strings. The function should 
count the number of times a string of "ice cream" appears inside these lists.

```js
count_ice_cream(["banana", "ice cream"]) =>  1

count_ice_cream(
  ["banana", "ice cream", [ "tofu", ["ice cream"] ], "ice cream" ]
)  => 3
```
"""


def count_ice_creams(food_list):
    count = 0

    for item in food_list:
        if isinstance(item, list):
            count += count_ice_creams(item)
        elif item == "ice cream":
            count += 1

    return count


def test_non_nested_list_single_element():
    assert count_ice_creams(["ice cream"]) == 1
    assert count_ice_creams(["not ice cream"]) == 0


def test_non_nested_list_multiple_ice_creams():
    some_ice_creams = ["ice cream", "banana", "ice cream", "apple"]
    assert count_ice_creams(some_ice_creams) == 2


def test_nested_list_single_item():
    nested_ice_cream = [[["ice cream"]]]
    assert count_ice_creams(nested_ice_cream) == 1

    nested_non_ice_cream = [[["not ice cream"]]]
    assert count_ice_creams(nested_non_ice_cream) == 0


def test_multiple_nested_items_varied_nesting():
    varied_nesting_search = [
        ["ice cream"],
        "sadness",
        [["ice cream"], "sadness"],
        [[["ice cream", "sadness"], "ice cream"]],
    ]

    assert count_ice_creams(varied_nesting_search) == 4
