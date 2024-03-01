def count_ice_creams(food_list):
    count = 0

    for item in food_list:
        if isinstance(item, list):
            count += count_ice_creams(item)
        elif item == "ice cream":
            count += 1

    return count


varied_nesting_search = [
    ["ice cream"],
    "sadness",
    [["ice cream"], "sadness"],
    [[["ice cream", "sadness"], "ice cream"]],
]

count_ice_creams(varied_nesting_search)
