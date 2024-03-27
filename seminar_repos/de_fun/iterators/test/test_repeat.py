from src.repeat import Repeat
from typing import Iterator
import pytest

# Test is it an iterator (correct methods)


@pytest.mark.it('Instance of Repeat should be an iterator')
def test_is_iterator():
    test_repeat = Repeat({}, times=1)

    assert isinstance(test_repeat, Iterator)


# Testing attributes
@pytest.mark.it('Repeat instance has necessary attributes')
def test_repeat_attributes():
    test_repeat = Repeat('', times=1)

    assert test_repeat.repeat_obj == ''
    assert test_repeat.times == 1


@pytest.mark.it('When passed no times argument, times should default to none')
def test_repeat_default_attribute():
    test_repeat = Repeat(1)

    assert test_repeat.times == None


# check that __iter__ returns self
@pytest.mark.it('When invoked with iter - should return reference to self')
def test_iter_returns_self():
    test_repeat = Repeat(3)

    assert iter(test_repeat) is test_repeat

# Check if next returns correct object - both no limit and with limit


@pytest.mark.it('When no limit is set, next should return object indefinitely')
def test_next_returns_object_indefinitely():
    test_repeat = Repeat(1)

    for _ in range(1000):
        assert next(test_repeat) == 1


@pytest.mark.it('When limit is set, next should return object')
def test_next_limit_set():
    test_repeat = Repeat(3, times=3)

    assert next(test_repeat) == 3
    assert next(test_repeat) == 3
    assert next(test_repeat) == 3

# Stop Iteration when limit is set


@pytest.mark.it('When limit is set, StopIteration should be raised when invoking next past the limit')
def test_raises_stop_iteration_exception():
    test_repeat = Repeat(3, times=3)

    next(test_repeat)
    next(test_repeat)
    next(test_repeat)

    with pytest.raises(StopIteration):
        next(test_repeat)
