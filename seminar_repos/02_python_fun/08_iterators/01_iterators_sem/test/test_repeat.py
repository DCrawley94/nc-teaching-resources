from src.repeat import Repeat
import pytest


# Testing attributes exist - object/times
def test_repeat_attributes_exists_on_instantiation():
    test_repeat = Repeat("abc", times=10)

    assert test_repeat.object == "abc"
    assert test_repeat.times == 10


# Test default attributes
def test_repeat_default_times_attribute():
    test_repeat = Repeat(1)

    assert test_repeat.times is None


# Test that iter of repeat returns self
def test_repeat_iter_returns_itself():
    test_repeat = Repeat({}, times=10)

    assert iter(test_repeat) is test_repeat


# no times: infinitely return object
def test_repeat_no_limit_next_returns_object_indefinitely():
    test_repeat = Repeat("hi")

    for _ in range(1000):
        assert next(test_repeat) == "hi"


# raise StopIteration - when times has been reached
def test_report_next_raises_stop_iteration_when_times_is_set():
    test_repeat = Repeat("hi", times=5)

    next(test_repeat)
    next(test_repeat)
    next(test_repeat)
    next(test_repeat)
    next(test_repeat)

    with pytest.raises(StopIteration):
        next(test_repeat)
