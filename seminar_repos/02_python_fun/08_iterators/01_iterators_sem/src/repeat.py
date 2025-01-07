"""
Reimplement the repeat iterator from the in-built itertools library.

Repeat should be instantiated with:
    - any type of Python object
    - times - integer representing the number of repeats *OPTIONAL*

If the times argument is specified then the object will be
    returned that number of times and no more

If the times argument is not specified then the object
    will be returned indefinitely
"""


class Repeat:
    def __init__(self, repeat_obj, times=None):
        self.repeat_obj = repeat_obj
        self.times = times
        self._repeat_count = 0

    # __iter__
    def __iter__(self):
        return self

    #  __next__
    def __next__(self):
        if self.times:
            if self._repeat_count < self.times:
                self._repeat_count += 1
                return self.repeat_obj
            else:
                raise StopIteration

        return self.repeat_obj
