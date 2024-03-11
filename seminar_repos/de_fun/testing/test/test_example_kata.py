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
