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
    assert sum_alphabet_indices('') == 0


def test_sum_alphabet_indices_returns_single_index_when_passed_single_char():
    assert sum_alphabet_indices('a') == 0
    assert sum_alphabet_indices('h') == 7


def test_sum_alphabet_indices_returns_sum_of_indices_when_passed_multiple_chars():
    assert sum_alphabet_indices('abc') == 3
    assert sum_alphabet_indices('hello') == 47


def test_sum_alphabet_indices_ignores_capitalised_letters():
    assert sum_alphabet_indices('aBc') == 2
    assert sum_alphabet_indices('Hello') == 40


def test_sum_alphabet_indices_ignores_non_alphabet_chars():
    assert sum_alphabet_indices('a dog 3!') == 23
```

Possible solution:

```py
def sum_alphabet_indices(sentence):
    total = 0

    for char in sentence:
        if char in ascii_lowercase:
            total += ascii_lowercase.index(char)

    return total
```
