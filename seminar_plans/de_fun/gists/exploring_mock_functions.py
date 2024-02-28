# ~~~~~ Example 1: copy and do something (map) ~~~~~

def copy_dict_and_do_something(given_dict, given_func):
    new_dict = {}
    for k, v in given_dict.items():
        new_dict[k] = given_func(v)

    # Can do a refactor job if you want to show off comprehensions again:
    # {k: given_func(v) for k, v in given_dict.items()}

    return new_dict

# Can make reasonable assertions about the output


def test_example_1_empty_dict():
    def test_fn(x):
        return x

    assert copy_dict_and_do_something({}, test_fn) == {}


def test_example_1_single_key():
    def test_fn(x):
        return x*2
    test_dict = {"num_1": 1}

    assert copy_dict_and_do_something(test_dict, test_fn) == {"num_1": 2}


def test_example_1_multiple_keys():
    def test_fn(x):
        return f"Hello {x}"

    test_dict = {"name_1": "Poonam", "name_2": "Danika"}

    assert copy_dict_and_do_something(test_dict, test_fn) == {
        "name_1": "Hello Poonam", "name_2": "Hello Danika"}


def test_example_1_returns_new_dict():
    def test_fn(x):
        return f"Hello {x}"

    test_dict = {"name_1": "Poonam", "name_2": "Danika"}

    assert copy_dict_and_do_something(test_dict, test_fn) is not test_dict


# However we could improve our tests by asserting about the function passed in
# Can demo the tests below or move onto the next example

def test_example_1_passed_func_is_invoked_correct_number_of_times():
    call_count = 0

    def test_fn(x):
        nonlocal call_count
        call_count += 1
        # Don't need to specify a return as we won't be checking it

    test_dict = {"name_1": "Poonam", "name_2": "Danika"}

    copy_dict_and_do_something(test_dict, test_fn)
    assert call_count == 2


def test_example_1_passed_func_is_invoked_with_correct_args():
    args = []

    def test_fn(x):
        args.append(x)
        # Don't need to specify a return as we won't be checking it

    test_dict = {"name_1": "Poonam", "name_2": "Danika"}

    copy_dict_and_do_something(test_dict, test_fn)
    assert args == ["Poonam", "Danika"]


# ~~~~~ Example 2: iterate_and_do_work (for_each) ~~~~~

def iterate_and_do_work(given_list, iteratee_func):
    for el in given_list:
        iteratee_func(el)

# Hammer home that for this we really don't care what the function is doing
# It just needs to be invoked correctly


def test_example_2_passed_func_is_invoked_correct_number_of_times():
    call_count = 0

    def test_fn(x):
        nonlocal call_count
        call_count += 1
        # Don't need to specify a return as we won't be checking it

    test_list = [1, 2, 3, 4, 5]

    iterate_and_do_work(test_list, test_fn)
    assert call_count == 5


def test_example_2_passed_func_is_invoked_with_correct_args():
    args = []

    def test_fn(x):
        args.append(x)
        # Don't need to specify a return as we won't be checking it

    test_list = [1, 2, 3, 4, 5]

    iterate_and_do_work(test_list, test_fn)
    assert args == [1, 2, 3, 4, 5]
