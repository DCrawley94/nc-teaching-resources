"""
iterate_and_do_work

- This function accepts a list and a function as its arguments and has no return value (None)

- This function should be invoked with each element of the list in turn.

- The original list should be unchanged
"""


def iterate_and_do_work(list_to_iterate, func):
    for item in list_to_iterate:
        func(item)
