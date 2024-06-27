# Iterator class

class ReversedIterator:
    def __init__(self, collection):
        self.collection = collection
        self._index = len(collection) - 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.collection[self._index]
        return value


class TestReversedIterator:
    @pytest.mark.it('Stores given collection as an attribute')
    def test_reversed_iterator_attributes(self):
        test_reverse_iterator = ReversedIterator([1,2,3])
        assert test_reverse_iterator.collection == [1,2,3]
        #  not testing index as it's an implementation detail


    @pytest.mark.it(
        'When invoked with iter a ReversedIterator instance should return itself')
    def test_reversed_iterator_iter_returns_self(self):
        test_reverse_iterator = ReversedIterator([1,2,3])

        assert iter(test_reverse_iterator) is test_reverse_iterator


    @pytest.mark.it(
        'First invocation of next should return the last element in collection')
    def test_reversed_iterator_next_first_invocation(self):
        test_reverse_iterator = ReversedIterator([1,2,3])
        assert next(test_reverse_iterator) == 3