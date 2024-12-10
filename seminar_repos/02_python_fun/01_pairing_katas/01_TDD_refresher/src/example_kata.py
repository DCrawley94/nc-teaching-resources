from string import ascii_lowercase


def sum_alphabet_indices(sentence):
    """
    - This function should take a **string** as argument and return an
        **integer**
    - That integer that is returned will be sum of the index positions of the
        string characters as they appear in the alphabet
        (taking into account zero indexing)
    - the function will ignore any characters that are not lowercase letters
    """
    # count = 0

    # for char in sentence:
    #     count += ascii_lowercase.index(char)

    return sum([ascii_lowercase.index(char) for char in sentence])
