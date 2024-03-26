class Repeat:
    def __init__(self, repeat_obj, times=None):
        self._repeat_obj = repeat_obj
        self._times = times
        # As this is tied to implementation can set this as a private attribute as a throwback to the previous week
        self._call_count = 0

    def __iter__(self):
        print('__iter__ called')
        return self

    def __next__(self):
        if self._times:
            # If a repeat limit is set then check the call count
            if self._call_count < self._times:
                self._call_count += 1
                print('__next__ called')
                return self._repeat_obj
            else:
                print('StopIteration raised')
                raise StopIteration
        return self._repeat_obj


r = Repeat(5, times=3)
print('iterator created: ', r)

print('beginning loop')
for _ in r:
    print('loop body')
