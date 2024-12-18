class Queue:
    def __init__(self, max_size):
        self.storage = {}
        self.back = 0
        self.front = 0
        self.max_size = max_size
