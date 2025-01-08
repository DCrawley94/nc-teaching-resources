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
    def __init__(self, object, times=None):
        self.object = object
        self.times = times
        self.counter = 0

    def __iter__(self):
        print("creating iterator...")
        return self

    def __next__(self):
        print("getting next value ...")
        if self.times:
            if self.counter < self.times:
                self.counter += 1
                return self.object
            else:
                raise StopIteration
        else:
            return self.object


r = Repeat("hi", times=5)

for v in r:
    print(v)
