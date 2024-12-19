class Queue:
    def __init__(self, max_size=5):
        self.storage = {}
        self.back = 0
        self.front = 0
        self.max_size = max_size

    def enqueue(self, item):
        if len(self.storage) < self.max_size:
            self.storage[self.back] = item
            self.back += 1


# A dequeue method that removes items from the front of the queue,
# provided the queue isn't already empty.
