from src.nc_map import NCMap
import pytest


class TestNCMap:
    def test_next_method(self):
        test_map = NCMap(lambda x: x, [1, 2, 3, 4, 5])
        for _ in range(5):
            next(test_map)

    def test_iter_self(self):
        test_map = NCMap(lambda x: x, [1, 2, 3, 4, 5])
        assert iter(test_map) is test_map

    def test_iterator_exhausted(self):
        test_map = NCMap(lambda x: x, [1, 2, 3, 4, 5])

        for _ in range(5):
            next(test_map)

        with pytest.raises(StopIteration):
            next(test_map)

    def test_applies_func(self):
        test_map = NCMap(lambda x: x * 2, [1, 2, 3, 4, 5])
        assert list(test_map) == [2, 4, 6, 8, 10]

    def xtest_single_iteration(self):
        test_map = NCMap(lambda x: x * 2, [1, 2, 3, 4, 5])
        assert len(list(test_map)) == 5
        assert len(list(test_map)) == 0
        assert len(list(test_map)) == 0
        assert len(list(test_map)) == 0
