"""
# count_ice_cream

- create a function that accepts a list as an argument
- this list will either contain strings or lists which can also contain strings
- The function should count the number of times a string of "ice cream"
    appears inside these lists.
"""


def count_ice_creams(food_list):
    count = 0

    for item in food_list:
        if isinstance(item, list):
            return count_ice_creams(item)
        elif item == "ice cream":
            count += 1

    return count
