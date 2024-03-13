# Testing HOFs

## Resources:

- [Figjam](https://www.figma.com/file/FCyLSfwkGyuQY3HI5pKaQk/Testing-HOFs?type=whiteboard&node-id=0-1&t=NDtLXPSUDjdGEDPr-0)

## Learning Objectives:

- Understand how we can use Mock functions to clearly define the behaviours being tested
- Know how to create a basic mock function

## First Task - TDD refresher and show `testdox`

**`copy_dict_and_update_values`**

Introduce the problem on figjam

Have some tests pre-written:

- empty dict
- single key
- multi key

And have start to a solution:

```py
def copy_dict_and_update_values(dict_to_update, func):
    for k, v in dict_to_update.items():
        dict_to_update[k] = func(v)

    return dict_to_update

```

Get students to help write the next tests and help solve it:

**They might need a refresher on how to do these tests**

```py
def test_copy_dict_and_update_values_returns_new_dict():
    def test_fn(x):
        return f"Hello {x}"

    test_dict = {"name_1": "Poonam", "name_2": "Danika"}

    assert copy_dict_and_do_something(test_dict, test_fn) is not test_dict
```

```py
def test_copy_dict_and_update_values_does_not_mutate_original():
    def test_fn(x):
        return f"Hello {x}"

    test_dict = {"name_1": "Poonam", "name_2": "Danika"}

    copy_dict_and_do_something(test_dict, test_fn)

    assert test_dict == {"name_1": "Poonam", "name_2": "Danika"}

```

After writing these tests ask students if these tests are enough or if they could be improved?

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

- Test number of invocations
- Test how the function was invoked
