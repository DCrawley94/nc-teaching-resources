# Pytest Refresher and AAA

## Learning Objectives

- Know how to set up a python virtual environment, ready for testing.
- Understand the steps of TDD (red-green-refactor)
- Use Arrange, Act, Assert pattern

## Intro

Introduce the repo and explain that we're gonna be working through a kata with TDD.

Show the repo structure: src/test

Nothing installed in the project so will be setting that up from scratch.

Ask students to guide me through the initial set up steps:

- create virtual environment
- start virtual environment
- install pytest to virtual environment
- set up PYTHONPATH? - only do this if students ask for it, can be left until I start running tests
- set local version? Can do this but not as important

## Introduce the problem itself

- On Figjam - also in README

## TDD Time

Pick on students

What would first test be etc.

Possible order of tests:

- empty string
- single char
- multiple chars
- ignores none lowercase letters

```py
from src.example_kata import sum_alphabet_indices


def test_sum_alphabet_indices_returns_0_when_passed_empty_string():
    # ARRANGE
    test_str = ''
    expected_result = 0

    # ACT
    result = sum_alphabet_indices(test_str)

    # ASSERT
    assert result == expected_result


def test_sum_alphabet_indices_returns_single_index_when_passed_single_char():
    test_str = "b"
    expected_result = 1

    result = sum_alphabet_indices(test_str)

    assert result == expected_result


    test_str_2 = "z"
    expected_result_2 = 25

    result_2 = sum_alphabet_indices(test_str_2)

    assert result_2 == expected_result_2


def test_sum_alphabet_indices_returns_sum_of_indices_when_passed_multiple_chars():
    test_str = 'cat'
    expected_result = 21

    result = sum_alphabet_indices(test_str)

    assert result == expected_result


def test_sum_alphabet_indices_ignores_capitalised_letters():
    assert sum_alphabet_indices('aBc') == 2
    assert sum_alphabet_indices('Hello') == 40


def test_sum_alphabet_indices_ignores_non_alphabet_chars():
    test_str = 'cat!'
    expected_result = 21

    result = sum_alphabet_indices(test_str)

    assert result == expected_result

```

Possible solution:

```py
from string import ascii_lowercase

def sum_alphabet_indices(sentence):
    total = 0

    for char in sentence:
        if char in ascii_lowercase:
            total += ascii_lowercase.index(char)

    return total
```

```py

def sum_alphabet_indices(sentence):
    total_sum = 0

    for char in sentence:
        if "a" <= char <= "z":
            total_sum += ord(char) - ord("a")

    return total_sum
```
