class NCMap:
    def __init__(self, func, iterable):
        self.func = func
        self.iterable = iterable
        self.index = 0

    def __next__(self):
        print("trying to get next value")
        if self.index < len(self.iterable):
            value = self.func(self.iterable[self.index])
            self.index += 1
            return value
        else:
            raise StopIteration

    def __iter__(self):
        print("creating iterator")
        return self


if __name__ == "__main__":

    def double(num):
        return num * 2

    m = NCMap(double, [5, 10, 15])
    print("starting loop")
    for el in m:
        print(el)
