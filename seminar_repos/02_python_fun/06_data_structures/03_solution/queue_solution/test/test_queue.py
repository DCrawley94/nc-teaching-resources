from src.queue import Queue


class TestAttributes:
    def test_storage_attribute(self):
        test_queue = Queue(10)
        assert test_queue.storage == {}

    def test_default_front_attribute(self):
        test_queue = Queue(10)
        assert test_queue.front == 0

    def test_default_back_attribute(self):
        test_queue = Queue(10)
        assert test_queue.back == 0

    def test_max_size_attribute(self):
        test_queue = Queue(10)
        assert test_queue.max_size == 10

    def test_max_size_default_attribute(self):
        test_queue = Queue()
        assert test_queue.max_size == 5
