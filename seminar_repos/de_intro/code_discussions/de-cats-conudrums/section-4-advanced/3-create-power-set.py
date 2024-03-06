# You will need to implement a function create_power_set()

# It will need to return an list of all possible sub-lists given some
#  starting list

# For example,
# create_power_set(['a', 'b', 'c']) should return

# [
#   [], ['a'], ['b'], ['c'],
#   ['a', 'b'], ['b', 'c'] ,
#   ['a', 'c'], ['a', 'b', 'c']
# ]

# all the possible sub-lists that can be constructed from 3 distinct elements
# There should be 2**3 = 8 different subsets in total

# You will need to write your own tests for this task to prove your function
#  is working correctly, we have written the first test for you

# define your function here:


def test_create_power_set_returns_an_list_including_empty_list_when_passed_an_empty_list():
    assert create_power_set([]) == [[]]
