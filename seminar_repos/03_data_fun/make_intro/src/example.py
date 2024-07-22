"""
# count_ice_cream

- create a function that accepts a list as an argument
- this list will either contain strings or lists which can also contain strings
- The function should count the number of times a string of "ice cream"
    appears inside these lists.
"""


def count_ice_creams(food_list):
    count = 0

    for el in food_list:
        if el == "ice cream":
            count += 1
        elif isinstance(el, list):
            count += count_ice_creams(el)

    return count


# count_ice_creams([["ice cream"], ["ice cream"]])
