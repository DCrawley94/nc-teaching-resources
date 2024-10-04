def indexer(input_text):
    if input_text and input_text[0].isalpha():
        yield 0

    spaces = [" ", "\n"]

    for i in range(len(input_text)):
        if input_text[i].isalpha() and input_text[i - 1] in spaces:
            yield i
