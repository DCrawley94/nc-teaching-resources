from src.example_kata import sum_alphabet_indices

# empty string -> returns 0


def test_sum_alphabet_indices_returns_0_when_passed_empty_string():
    # ARRANGE
    input_str = ""
    expected_output = 0

    # ACT
    result = sum_alphabet_indices(input_str)

    # ASSERT
    assert result == expected_output


def test_sum_alphabet_indices_returns_single_index_when_passed_single_character_string():
    # ARRANGE
    input_str = "a"
    expected_output = 0

    # ACT
    result = sum_alphabet_indices(input_str)

    # ASSERT
    assert result == expected_output

    input_str = "z"
    expected_output = 25

    result = sum_alphabet_indices(input_str)

    assert result == expected_output


def test_sum_alphabet_indices_returns_sum_of_indices_when_passed_multi_character_string():
    input_str = "cat"
    expected_output = 21

    result = sum_alphabet_indices(input_str)

    assert result == expected_output


def test_sum_alphabet_indices_ignores_non_alphabet_chars():
    input_str = "cat!"
    expected_output = 21

    result = sum_alphabet_indices(input_str)

    assert result == expected_output


def test_sum_alphabet_indices_ignores_non_lowercase_chars():
    input_str = "aBc"
    expected_output = 2

    result = sum_alphabet_indices(input_str)

    assert result == expected_output
