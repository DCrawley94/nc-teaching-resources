def filter_odd_numbers(numbers):
    return [n for n in numbers if n % 2 != 0]


def double_numbers(numbers):
    return [n * 2 for n in numbers]


def process_numbers(numbers, filter_func, transform_func):
    """
    This function processes a given list of numbers, first by filtering the
    list using the given filter function, and then transforming the remaining
    numbers. Finally the sum of the numbers is returned.

    Args:
        numbers: list of integers
        filter_func: function for filtering a list of numbers
        transform_func: function for transforming a list of numbers
    """
    filtered_numbers = filter_func(numbers)
    print(f"filtered numbers: {filtered_numbers}")

    transformed_numbers = transform_func(filtered_numbers)
    print(f"transformed numbers: {transformed_numbers}")

    total = sum(transformed_numbers)
    return total


print(process_numbers([1, 2, 3, 4, 5], filter_odd_numbers, double_numbers))
