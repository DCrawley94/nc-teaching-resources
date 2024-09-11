def process_numbers(numbers, filter_func, transform_func=None):
    """
    This function processes a given list of numbers, first by filtering the
    list using the given filter function, and then transforming the remaining
    numbers. Finally the sum of the numbers is returned.

    Args:
        numbers: list of integers
        filter_func: function for filtering a list of numbers
        *OPTIONAL* transform_func: function for transforming a list of numbers
    """
    processed_numbers = filter_func(numbers)
    if transform_func:
        processed_numbers = transform_func(processed_numbers)
    return sum(processed_numbers)
