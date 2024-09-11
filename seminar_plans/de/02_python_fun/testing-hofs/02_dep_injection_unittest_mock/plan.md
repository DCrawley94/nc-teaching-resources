# Dependency Injection and `unittest.mock`

## Learning Objectives

## Plan

### Intro

Introduce the session, tell students that we will be looking at two different functions and discussing the pros/cons of the two approaches. Give them warning that I will be picking on people so they should be thinking about these pros and cons while watching.

Demo two functions, while explaining that functionally they achieve the same goal.

### Figjam Discussion:

**Example 1**

Negatives of this approach include:

1. Hard to Understand: (admittedly this contrived example is fairly simple but hopefully students can see how the problems may arise in their code)

   The function does several things (filtering, doubling) all at once. This makes it harder to read and understand at a glance, especially for someone new to the code.

2. Difficult to Maintain:

   If you need to change how one part of the process works (like filtering), you have to dig into the code to make changes. increasing the risk of breaking code and introducing bugs.

3. Limited Reusability:

   The function is tightly coupled to specific tasks (filtering odd numbers, doubling them, and summing). If you want to reuse part of this logic (like just the filtering or doubling), you have to rewrite it elsewhere. **This is not DRY 😱**

4. Harder to test:

   Testing the function is more difficult because it does multiple things at once. If there’s a bug, it’s harder to pinpoint which part of the process is causing the problem.

5. Lack of Flexibility:

   You can't easily change what the function does without modifying its internal logic. For example, if you wanted to filter even numbers instead or apply a different transformation, you would have to rewrite parts of the function.

**Example 2**

The benefits of this approach are summarised below:

1. Modularity:

   The refactored version separates the concerns into 1 wrapper function and 2 distinct utility functions: filter_odd_numbers and double_numbers. This makes each function simpler and easier to understand.

2. Dependency Injection:

   By passing the utility functions as arguments to process_numbers, we achieve loose coupling. The main function doesn't need to know the details of how filtering or transforming is done. It just uses the functions provided to it.

   In computing and systems design, a loosely coupled system is one:

   - in which components are weakly associated (have breakable relationships) with each other, and thus changes in one component least affect existence or performance of another component.
   - in which each of its components has, or makes use of, little or no knowledge of the definitions of other separate components. Subareas include the coupling of classes, interfaces, data, and services. Loose coupling is the opposite of tight coupling.

3. Flexibility:

   The refactored function can now be reused with different filtering and transforming functions without any changes to its core logic. This promotes reusability and adaptability to new requirements.

It could even be improved by extracting the `sum` logic, what if we wanted to aggregate the data in a different way?

### Task - Build and test a function that is similar to example 2

Show students the function definition and ask them how we might go about testing it.

Hopefully they start suggesting things like an empty array of numbers:

**Highlight that the function expects a filter function even if it's not going to be used**

```py
def test_process_numbers_returns_empty_list_when_passed_empty_list():
    def test_filter_fn(val):
        return val

    assert process_numbers([], test_filter_fn) == 0
```

Can move onto testing that the result of calling the filter function is summed up:

**also emphasise that it might be useful to check if the filter function has been invoked**

```py
def test_process_numbers_applies_given_filter_function_to_the_input_list():
    has_been_called = False

    def test_filter_fn(input_list):
        nonlocal has_been_called
        has_been_called = True
        return [1, 2, 3]

    assert process_numbers([1, 2, 3, 4, 5], test_filter_fn) == 6
    assert has_been_called is True
```

Possible Solution:

```py
def process_numbers(numbers, filter_func, transform_func=None):
    """
    This function processes a given list of numbers, first by filtering the
    list using the given filter function, and then transforming the remaining
    numbers. Finally the sum of the numbers is returned.

    Args:
        numbers: list of integers
        filter_func: function for filtering a list of numbers
        transform_func: function for transforming a list of numbers
    """
    processed_numbers = filter_func(numbers)
    print(f"filtered numbers: {processed_numbers}")

    if transform_func:
        processed_numbers = transform_func(processed_numbers)

    print(f"transformed numbers: {processed_numbers}")

    total = sum(processed_numbers)
    return total
```
