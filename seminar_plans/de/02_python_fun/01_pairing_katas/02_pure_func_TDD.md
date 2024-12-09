# Pure Functions and Immutability

Introduce the problem on Figjam [link](https://www.figma.com/board/YwULSdLcEBiRj9ofmxqGM2/Pure-Function-Testing?node-id=0-1&t=4BbrE7MdKjD4lwG2-1), when talking through it emphasise that the functions returns a **new** dictionary and is a **pure** function.

## TDD

Get students to lead me through TDD, utilise **arrange**/**act**/**assert** for all tests.

Possible build up of tests:

- empty list (only do this if students suggest it) - can discuss benefits of this (if this fails then something has gone very wrong) vs the negatives (is this really testing the happy path/actual behaviour?)
- single profile that's already Python
- single profile non Python
- **At this point push for mutation/reference tests** - at this point it might be good to questions students on the difference between `copy`/`deepcopy`
- multiple profile non Python

Might need to force certain tests to fail

Possible solution:

```py
def correct_language(profiles):
    new_profiles = deepcopy(profiles)
    for profile in new_profiles:
        profile["language"] = "Python"
    return new_profiles

```

Example tests:

```py

def test_correct_language_returns_a_new_list():
    # arrange
    input1 = [
        {"name": "Kyle", "language": "Javascript"},
        {"name": "Liam", "language": "Go"}
    ]
    # act
    result = correct_language(input1)

    # assert
    assert result is not input1


def test_correct_language_does_not_mutate_input():
    # arrange
    input1 = [
        {"name": "Kyle", "language": "Javascript"},
        {"name": "Liam", "language": "Go"}
    ]
    expected_input = [
        {"name": "Kyle", "language": "Javascript"},
        {"name": "Liam", "language": "Go"}
    ]
    # act
    correct_language(input1)

    # assert
    assert input1 == expected_input


def test_correct_language_does_not_change_profiles_when_language_is_python():
    # arrange
    input1 = [{"name": "Kyle", "language": "Python"}]
    expected = [{"name": "Kyle", "language": "Python"}]
    # act
    result = correct_language(input1)

    # assert
    assert result == expected


def test_changes_language_of_single_non_Python_profile():
    # arrange
    input1 = [{"name": "Liam", "language": "Javascript"}]
    expected = [{"name": "Liam", "language": "Python"}]
    # act
    result = correct_language(input1)

    # assert
    assert result == expected


def test_changes_language_of_multiple_non_Python_profiles():
    # arrange
    input1 = [
        {"name": "Kyle", "language": "Javascript"},
        {"name": "Liam", "language": "Go"}
    ]
    expected = [
        {"name": "Kyle", "language": "Python"},
        {"name": "Liam", "language": "Python"}
    ]
    # act
    result = correct_language(input1)

    # assert
    assert result == expected
```
