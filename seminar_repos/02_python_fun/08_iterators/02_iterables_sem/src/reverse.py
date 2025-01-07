class ReversedIterator:
    def __init__(self, collection):
        self.collection = collection

    def __iter__(self):
        return self

    def __next__(self):
        pass


class ReversedIterable:
    pass
