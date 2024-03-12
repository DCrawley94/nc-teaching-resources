# Testing HOFs

## Resources:

- [Figjam](https://www.figma.com/file/FCyLSfwkGyuQY3HI5pKaQk/Testing-HOFs?type=whiteboard&node-id=0-1&t=NDtLXPSUDjdGEDPr-0)

## Learning Objectives:

- Understand how we can use Mock functions to clearly define the behaviours being tested
- Know how to create a basic mock function

## First task - TDD refresher and show `testdox`

**`copy_dict_and_update_values`**

Introduce the problem on figjam

Have some tests pre-written:

- empty dict
- single key

And have start to a solution:

```py
def copy_dict_and_update_values(given_dict, given_func):
    new_dict = {}
    for k, v in given_dict.items():
        new_dict[k] = given_func(v)

    # Can do a refactor job if you want to show off comprehensions again:
    # {k: given_func(v) for k, v in given_dict.items()}

    return new_dict

```

Get students to help write the next test and help solve it:

```py
def test_example_1_multiple_keys():
    def test_fn(x):
        return f"Hello {x}"

    test_dict = {"name_1": "Poonam", "name_2": "Danika"}

    assert copy_dict_and_do_something(test_dict, test_fn) == {
        "name_1": "Hello Poonam", "name_2": "Hello Danika"}
```
