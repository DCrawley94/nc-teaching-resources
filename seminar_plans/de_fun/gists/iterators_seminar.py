import pytest


# Re-implement functools.repeat: https://docs.python.org/3/library/itertools.html#itertools.repeat
class Repeat:
    def __init__(self, repeat_obj, times=None):
        self.repeat_obj = repeat_obj
        self.times = times
        # As this is tied to implementation can set this as a private attribute as a throwback to the previous week
        self.__call_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.times:
            # If a repeat limit is set then check the call count
            if self.__call_count < self.times:
                self.__call_count += 1
                return self.repeat_obj
            else:
                raise StopIteration
        return self.repeat_obj


@pytest.mark.it('Repeat instance has the correct attributes')
def test_repeat_attributes():
    test_repeat = Repeat(5, times=3)

    assert test_repeat.repeat_obj == 5
    assert test_repeat.times == 3


@pytest.mark.it('When passed no times argument, times should default to None')
def test_repeat_default_attribute():
    test_repeat = Repeat(5)

    assert test_repeat.times == None


@pytest.mark.it('When invoked with iter a repeat instance should return itself')
def test_iter_returns_self():
    test_repeat = Repeat(5)

    assert iter(test_repeat) is test_repeat


@pytest.mark.it('When no limit is set, given object should be returned indefinitely when invoked with next')
def test_repeat_returns_object_indefinitely():
    test_repeat = Repeat(5)

    for _ in range(1000):
        assert next(test_repeat) == 5


@pytest.mark.it('When a limit is set, given object should be returned no more than the given value for times')
def test_repeat_with_times():
    test_repeat = Repeat(5, times=3)

    next(test_repeat)
    next(test_repeat)
    next(test_repeat)

    with pytest.raises(StopIteration):
        next(test_repeat)
