def process_numbers(numbers):
    """
    This function processes a given list of numbers, first by removing the
    even numbers and then by doubling the remaining numbers. Finally the
    sum of the numbers is returned.

    Args:
        numbers: list of integers
    """
    filtered_numbers = [n for n in numbers if n % 2 != 0]
    print(f"filtered numbers: {filtered_numbers}")

    doubled_numbers = [n * 2 for n in filtered_numbers]
    print(f"doubled numbers: {doubled_numbers}")

    total = sum(doubled_numbers)

    return total


print(process_numbers([1, 2, 3, 4, 5]))
