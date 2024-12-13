from src.example import iterate_and_do_work


# - function returns None


def test_iterate_and_do_work_returns_none():
    # Arrange
    def test_fn(x):
        pass

    input_list = [1, 2, 3]

    # Act
    result = iterate_and_do_work(input_list, test_fn)

    # Assert
    assert result == None


# - test the number of invocations
#   - empty list > call count == 0
#   - list with elements > call count  == length of list


def test_given_func_not_invoked_when_given_list_is_empty():
    # Arrange
    call_count = 0
    test_list = []

    def test_fn(x):
        nonlocal call_count
        call_count += 1

    # Act
    iterate_and_do_work(test_list, test_fn)

    # Assert
    assert call_count == 0


def test_given_func_is_invoked_once_for_each_list_element():
    # Arrange
    call_count = 0
    test_list = [1, 2, 3, 4, 5]

    def test_fn(x):
        nonlocal call_count
        call_count = call_count + 1

    # Act
    iterate_and_do_work(test_list, test_fn)

    # Assert
    assert call_count == 5


# - test how the given function is invoked
def test_given_func_is_invoked_with_correct_args():
    # Arrange
    args = []
    test_list = [1, 2, 3, 4, 5]

    def test_fn(x):
        args.append(x)

    # Act
    iterate_and_do_work(test_list, test_fn)

    # Assert
    assert args == [1, 2, 3, 4, 5]


# - Test for mutation
def test_iterate_and_do_work_does_not_mutate_input_list():
    test_list = [1, 2, 3, 4, 5]

    def test_fn(x):
        pass

    iterate_and_do_work(test_list, test_fn)

    assert test_list == [1, 2, 3, 4, 5]


# def test_iterate_and_do_work_returns_different_reference():
#     test_list = [1, 2, 3, 4, 5]

#     def test_fn(x):
#         pass

#     result = iterate_and_do_work(test_list, test_fn)

#     assert result is not test_list
