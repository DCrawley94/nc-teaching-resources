class ReversedIterator:
    def __init__(self, collection):
        self.collection = collection
        self._index = len(collection) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < 0:
            raise StopIteration
        value = self.collection[self._index]
        self._index -= 1
        return value


class ReversedIterable:
    def __init__(self, collection):
        self.collection = collection

    def __iter__(self):
        return ReversedIterator(self.collection)


l1 = [1, 2, 3, 4, 5]

iterator = ReversedIterator(l1)

for el in iterator:
    # calls iter then next
    print(el)

iterator = ReversedIterator(l1)

for el in iterator:
    # calls iter then next
    print(el)


# iterable = ReversedIterable(l1)


# for el in iterable:
#     # calls iter then next
#     print(el)

# for el in iterable:
#     # calls iter then next
#     print(el)
