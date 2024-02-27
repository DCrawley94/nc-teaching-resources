def copy_dict_and_do_something(given_dict, given_func):
    new_dict = {}
    for k, v in given_dict.items():
        new_dict[k] = given_func(v)

    return new_dict

# Can make reasonable assertions about the output


def test_empty_dict():
    def test_fn(x):
        return x

    assert copy_dict_and_do_something({}, test_fn) == {}


def test_single_key():
    def test_fn(x):
        return x*2
    test_dict = {"num_1": 1}

    assert copy_dict_and_do_something(test_dict, test_fn) == {"num_1": 2}


def test_multiple_keys():
    def test_fn(x):
        return f"Hello {x}"

    test_dict = {"name_1": "Poonam", "name_2": "Danika"}

    assert copy_dict_and_do_something(test_dict, test_fn) == {
        "name_1": "Hello Poonam", "name_2": "Hello Danika"}


def test_returns_new_dict():
    def test_fn(x):
        return f"Hello {x}"

    test_dict = {"name_1": "Poonam", "name_2": "Danika"}

    assert copy_dict_and_do_something(test_dict, test_fn) is not test_dict


# However we could improve our tests by asserting about the function passed in
# Can demo the tests below or move onto the next example

def test_passed_func_is_invoked_correct_number_of_times():
    call_count = 0

    def test_fn(x):
        nonlocal call_count
        call_count += 1
        return f"Hello {x}"

    test_dict = {"name_1": "Poonam", "name_2": "Danika"}
