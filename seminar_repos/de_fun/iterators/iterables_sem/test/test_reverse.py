import pytest
from src.reverse import ReversedIterator, ReversedIterable


class TestReversedIterator:
    @pytest.mark.it('Stores given collection as an attribute')
    def test_reversed_iterator_attributes(self):
        test_reverse_iterator = ReversedIterator([1, 2, 3])
        assert test_reverse_iterator.collection == [1, 2, 3]

    @pytest.mark.it(
        'When invoked with iter a ReversedIterator instance should return '
        'itself')
    def test_reversed_iterator_iter_returns_self(self):
        test_reverse_iterator = ReversedIterator([1, 2, 3])

        assert iter(test_reverse_iterator) is test_reverse_iterator

    @pytest.mark.it(
        'First invocation of next should return the last element in collection'
    )
    def test_reversed_iterator_next_first_invocation(self):
        test_reverse_iterator = ReversedIterator([1, 2, 3])
        assert next(test_reverse_iterator) == 3

    @pytest.mark.it(
        'Subsequent invocations of next should return elements in return order')
    def test_reversed_iterators_subsequent_next_invocations(self):
        test_reverse_iterator = ReversedIterator([1, 2, 3])

        assert next(test_reverse_iterator) == 3
        assert next(test_reverse_iterator) == 2
        assert next(test_reverse_iterator) == 1

    @pytest.mark.it(
        'StopIteration exception is raised after elements of collection are exhausted')
    def test_reversed_iterator_raises_stop_iteration(self):
        test_reverse_iterator = ReversedIterator([1, 2, 3])

        for _ in range(3):
            next(test_reverse_iterator)

        with pytest.raises(StopIteration):
            next(test_reverse_iterator)

    @pytest.mark.it('Can only be iterated over once')
    def test_reversed_iterator_single_iteration(self):
        test_reverse_iterator = ReversedIterator([1, 2, 3])

        lst_1 = list(test_reverse_iterator)

        lst_2 = list(test_reverse_iterator)

        assert lst_1 == [3, 2, 1]
        assert not lst_2


# __init__
class TestReversedIterable:

    @pytest.mark.it('Iterable instance has a collection attribute')
    def test_iterables_attributes(self):
        test_reverse_iterable = ReversedIterable([1, 2, 3])
        assert test_reverse_iterable.collection == [1, 2, 3]

# __iter__
    @pytest.mark.it('iter method should return reversed iterator instance')
    def test_reverse_iterables_instantiates_iterator(self):
        test_reverse_iterable = ReversedIterable([1, 2, 3])

        assert isinstance(iter(test_reverse_iterable), ReversedIterator)

    def test_reversed_iterable_iter_multi_instances(self):
        test_reverse_iterable = ReversedIterable([1, 2, 3])

        test_iterator_1 = iter(test_reverse_iterable)
        test_iterator_2 = iter(test_reverse_iterable)

        assert test_iterator_1 is not test_iterator_2
