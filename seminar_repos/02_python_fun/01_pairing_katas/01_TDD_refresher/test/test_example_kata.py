from src.example_kata import sum_alphabet_indices


# empty string > returns zero
def test_empty_string_returns_zero():
    # Arrange
    test_input = ""
    expected_output = 0

    # Act
    result = sum_alphabet_indices(test_input)

    # Assert
    assert result == expected_output


# single char > returns correct index
def test_single_chars_returns_correct_index():
    # Arrange
    test_input = "a"
    expect_output = 0

    # Act
    result = sum_alphabet_indices(test_input)

    # Assert
    assert result == expect_output

    # Arrange
    test_input_2 = "g"
    expect_output_2 = 6

    # Act
    result_2 = sum_alphabet_indices(test_input_2)

    # Assert
    assert result_2 == expect_output_2


def test_multi_character_strings_returns_sum_of_index_positions():
    # Arrange
    test_input = "bc"
    expect_output = 3

    # Act
    result = sum_alphabet_indices(test_input)

    # Assert
    assert result == expect_output
