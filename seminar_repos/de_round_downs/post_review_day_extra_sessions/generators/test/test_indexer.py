from src.indexer import indexer
import pytest


@pytest.fixture(scope="function")
def file_data():
    with open("test/sonnet18.txt", "r") as f:
        text = f.read()
    return text


class TestIndexer:
    def test_returns_empty_generator_for_empty_string(self):
        text = ""
        result = indexer(text)
        with pytest.raises(StopIteration):
            next(result)

    def test_has_leading_index_zero_for_non_empty_input(self):
        text1 = "Hello"
        text2 = "Hello Dolly"
        text3 = "The moon shines bright. In such a night as this,"

        assert next(indexer(text1)) == 0
        assert next(indexer(text2)) == 0
        assert next(indexer(text3)) == 0

    def test_correctly_indexes_single_line_text(self):
        text1 = "Hello"
        text2 = "Hello Dolly"
        text3 = "The moon shines bright. In such a night as this,"
        res1 = indexer(text1)

        assert next(res1) == 0
        assert list(indexer(text2)) == [0, 6]
        assert list(indexer(text3)) == [0, 4, 9, 16, 24, 27, 32, 34, 40, 43]
        with pytest.raises(StopIteration):
            next(res1)

    def test_does_not_index_leading_or_repeated_space(self):
        text = "  Space,   the final   frontier  "

        assert list(indexer(text)) == [2, 11, 15, 23]

    def test_deals_correctly_with_newline_characters(self):
        text = """The\nEnd"""
        assert list(indexer(text)) == [0, 4]

    def test_deals_correctly_with_multiline_text_read_from_file(self, file_data):
        indexed = indexer(file_data)
        listed_indexes = list(indexed)
        assert len(listed_indexes) == 114
        assert listed_indexes[0:4] == [0, 6, 8, 16]
        assert listed_indexes[33] == 173
