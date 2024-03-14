# Testing HOFs

## Resources:

- [Figjam](https://www.figma.com/file/FCyLSfwkGyuQY3HI5pKaQk/Testing-HOFs?type=whiteboard&node-id=0-1&t=NDtLXPSUDjdGEDPr-0)

## Learning Objectives:

- Understand how we can use Mock functions to clearly define the behaviours being tested
- Know how to create a basic mock function

## First Task - TDD refresher and show `testdox`

**`copy_dict_and_update_values`**

Introduce the problem on figjam

Talk about the kind of tests we could write - note these down and separate them into testing output vs. testing implementation.

- Are these tests are enough or if they could be improved?

Hopefully students suggest using mock functions but if not:

- The tests we've written so far give us reasonable confidence that our code is working as hoped.

- However we could improve confidence by adding tests asserting that the functions that's passed in is used correctly.

> How could we do that? 🤔 🤔 🤔 🤔 🤔

- Mock/Spy. Checking that function is invoked the correct number of times and with the correct arguments

- Depending on time can implement these tests but can also skip and use them for the next function

## Second Task - Mocks are required

Introduce second task: `iterate_and_do_work`

Explain clearly how the function could be used.

Ask students to identify what we could test to ensure that `iterate_and_do_work` is working properly.

- Test that passed function is invoked
- Test number of invocations
- Test how the function was invoked

```py
def iterate_and_do_work(given_list, iteratee_func):
    for el in given_list:
        iteratee_func(el)

# Hammer home that for this we really don't care what the function is doing
# It just needs to be invoked correctly


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

```
