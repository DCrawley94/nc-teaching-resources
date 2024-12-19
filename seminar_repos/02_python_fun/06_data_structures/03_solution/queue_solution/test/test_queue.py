from src.queue import Queue
import pytest


class TestAttributes:
    @pytest.mark.it("Storage should be set to default empty dictionary")
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


class TestEnqueue:
    # Test item is added to strage dictionary
    def test_item_is_added_to_storage(self):
        test_queue = Queue()
        test_queue.enqueue("apple")

        assert test_queue.storage == {0: "apple"}

    # Test back property in incremented
    def test_multiple_items_added_update_back_attribute(self):
        test_queue = Queue()

        test_queue.enqueue("apple")
        assert test_queue.back == 1

        test_queue.enqueue("orange")
        assert test_queue.back == 2

        assert test_queue.storage == {0: "apple", 1: "orange"}

    # Test that no more items added if queue is full
    def test_no_more_items_added_when_queue_is_full(self):
        test_queue = Queue(1)

        test_queue.enqueue("apple")
        test_queue.enqueue("orange")

        assert test_queue.back == 1
        assert test_queue.storage == {0: "apple"}


class TestDequeue:
    pass


# remove the first item from storage
# increment the front attribute
# if storage is empty - no action taken
