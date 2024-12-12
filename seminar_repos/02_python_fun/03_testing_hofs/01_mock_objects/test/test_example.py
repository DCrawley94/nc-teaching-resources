from example import iterate_and_do_work


def test_input_is_not_mutated():
    input_1 = [1, 2, 3]
    expected = [1, 2, 3]

    def test_func(arg):
        pass

    iterate_and_do_work(input_1, test_func)

    assert input_1 == expected


def test_function_returns_none():
    input_1 = [1, 2, 3]

    def test_func(arg):
        pass

    assert iterate_and_do_work(input_1, test_func) is None


def test_passed_function_is_invoked():
    input_1 = [1, 2, 3]
    counter = 0

    def test_func(arg):
        nonlocal counter
        counter += 1

    iterate_and_do_work(input_1, test_func)

    assert counter > 0


def test_passed_function_is_invoked_once_for_each_element():
    input_1 = [1, 2, 3]
    counter = 0

    def test_func(arg):
        nonlocal counter
        counter += 1

    iterate_and_do_work(input_1, test_func)

    assert counter == len(input_1)


def test_passed_function_is_invoked_with_correct_arguments():
    input_1 = [1, 2, 3]
    args = []

    def test_func(arg):
        nonlocal args
        args.append(arg)

    iterate_and_do_work(input_1, test_func)

    assert args == [1, 2, 3]
