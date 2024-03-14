from example import iterate_and_do_work


def test_iterate_and_do_work_invokes_passed_function():
    is_invoked = False

    def test_fn(x):
        nonlocal is_invoked
        is_invoked = True
        # Don't need to specify a return as we won't be checking it

    test_list = [1]

    iterate_and_do_work(test_list, test_fn)
    assert is_invoked


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
