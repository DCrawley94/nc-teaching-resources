"""
Reimplement the repeat iterator from the in-built itertools library.

A repeat instance will:
accept an object and an optional times argument
If the times argument is specified then the object will be returned that number of times and no more
If the times argument is not specified then the object will be returned indefinitely
"""


class Repeat:
    def __init__(self, repeat_obj, times=None):
        self.repeat_obj = repeat_obj
        self.times = times
        self.__call_count = 0

    # __iter__
    def __iter__(self):
        print('invoking iter')
        return self

    #  __next__
    def __next__(self):
        print('invoking next')
        if self.times:
            if self.__call_count < self.times:
                self.__call_count += 1
                return self.repeat_obj
            else:
                print('raising stop iteration')
                raise StopIteration
        return self.repeat_obj


repeat_iterator = Repeat(1)

print('starting loop')
for el in repeat_iterator:
    print(el)
print('finished loop')
