# Queue

## Solution

```py
class Queue:
    def __init__(self, max_size=5):
        self.storage = {}
        self.back = 0
        self.front = 0
        self.max_size = max_size

    def enqueue(self, item):
        if self.back - self.front < self.max_size:  # can refactor to use get_quantity when it exists!!
            self.storage[self.back] = item
            self.back += 1

    def dequeue(self):
        if self.front != self.back:
            del self.storage[self.front]
            self.front += 1

    def get_quantity(self):
        return self.back-self.front

    def is_empty(self):
        return self.get_quantity() == 0

    def is_full(self):
        return self.max_size == self.get_quantity()
```

## Tests

```py
class TestProperties:

    @pytest.mark.it("has storage property initialised as empty dict")
    def test_storage_property(self):
        test_queue = Queue()
        assert test_queue.storage == {}

    @pytest.mark.it("has default max_size of 5 if no arguments given")
    def test_max_size_default_property(self):
        test_queue = Queue()
        assert test_queue.max_size == 5

    @pytest.mark.it("has max_size property set by passed argument")
    def test_max_size_set_property(self):
        test_queue = Queue(max_size=12)
        assert test_queue.max_size == 12

    @pytest.mark.it("has default front property set to 0")
    def test_default_front_property(self):
        test_queue = Queue()
        assert test_queue.front == 0

    @pytest.mark.it("has default back property set to 0")
    def test_default_back_property(self):
        test_queue = Queue()
        assert test_queue.back == 0


class TestEnqueueMethod:
    @pytest.mark.it('adds item to the back of queue storage')
    def test_adds_item_to_queue(self):
        test_queue = Queue()
        test_queue.enqueue('apple')
        assert test_queue.storage == {0: 'apple'}

    @pytest.mark.it('does not add item if the queue is full')
    def test_does_not_add_item_to_queue(self):
        test_queue = Queue(0)
        test_queue.enqueue('apple')
        assert test_queue.storage == {}


class TestDequeueMethod:
    @pytest.mark.it('removes item from front of storage')
    def test_removes_item_from_queue(self):
        test_queue = Queue()
        test_queue.enqueue('apple')
        test_queue.enqueue('orange')
        test_queue.enqueue('pear')

        test_queue.dequeue()
        assert test_queue.storage == {1: 'orange', 2: 'pear'}

    @pytest.mark.it('removes item from front of storage multiple times')
    def test_removes_item_from_queue_multiple(self):
        test_queue = Queue()
        test_queue.enqueue('apple')
        test_queue.enqueue('orange')
        test_queue.enqueue('pear')

        test_queue.dequeue()
        test_queue.dequeue()

        assert test_queue.storage == {2: 'pear'}

    @pytest.mark.it('does not remove item when queue is empty')
    def test_no_removal_when_empty_queue(self):
        test_queue = Queue()
        test_queue.enqueue('apple')
        test_queue.enqueue('orange')

        test_queue.dequeue()
        test_queue.dequeue()
        test_queue.dequeue()

        assert test_queue.storage == {}


class TestGetQuantityMethod:
    @pytest.mark.it("returns number of items in the queue")
    def test_returns_queue_size(self):
        test_queue = Queue()
        assert test_queue.get_quantity() == 0

        test_queue.enqueue('apple')
        test_queue.enqueue('apple')
        assert test_queue.get_quantity() == 2


class TestIsEmptyMethod:
    @pytest.mark.it("returns True if queue is empty")
    def test_empty_queue_is_True(self):
        test_queue = Queue()

        assert test_queue.is_empty() == True

    @pytest.mark.it("returns False if queue is not empty")
    def test_not_empty_queue_is_False(self):
        test_queue = Queue()
        test_queue.enqueue('apple')

        assert test_queue.is_empty() == False


class TestIsFullMethod:
    @pytest.mark.it("returns True if queue is full")
    def test_full_queue_is_True(self):
        test_queue = Queue(max_size=2)
        test_queue.enqueue('apple')
        test_queue.enqueue('apple')

        assert test_queue.is_full() == True

    @pytest.mark.it("returns False if queue is eempty")
    def test_empty_queue_is_False(self):
        test_queue = Queue()

        assert test_queue.is_full() == False

    @pytest.mark.it("returns False if queue is not full")
    def test_not_full_queue_is_False(self):
        test_queue = Queue()
        test_queue.enqueue('apple')
        test_queue.enqueue('orange')
        assert test_queue.is_full() == False
```

## Flow

### Pre-made Attributes

- Test default max-size is failing. How we fix?

## `enqueue`

What are the behaviour we wanna test?

- adds item to the back of the queue
- can it be called multiple times?
- but **only** if there is space!

Example:

```py
    def test_adds_item_to_queue(self):
        test_queue = Queue()
        test_queue.enqueue('apple')
        assert test_queue.storage == {0: 'apple'}


    def test_adds_item_to_queue(self):
        test_queue = Queue(0)
        test_queue.enqueue('apple')
        assert test_queue.storage == {}
```

Possible solution:

```py
def enqueue(self, item):
    if self.back - self.front < self.max_size:  # can refactor to use get_quantity when it exists!!
        self.storage[self.back] = item
        self.back += 1
```

## `dequeue`

What are the behaviour we wanna test?

- removes item from the front of the queue
- can we call it multiple times?
- what happens if the queue is empty?

Example:

```py
    def test_removes_item_from_queue(self):
        test_queue = Queue()
        test_queue.enqueue('apple')
        test_queue.enqueue('orange')
        test_queue.enqueue('pear')

        test_queue.dequeue()
        assert test_queue.storage == {1: 'orange', 2: 'pear'}

    def test_removes_item_from_queue_multiple(self):
        test_queue = Queue()
        test_queue.enqueue('apple')
        test_queue.enqueue('orange')
        test_queue.enqueue('pear')

        test_queue.dequeue()
        test_queue.dequeue()

        assert test_queue.storage == {2: 'pear'}

    def test_no_removal_when_empty_queue(self):
        test_queue = Queue()
        test_queue.enqueue('apple')
        test_queue.enqueue('orange')

        test_queue.dequeue()
        test_queue.dequeue()
        test_queue.dequeue()

        assert test_queue.storage == {}
```

Possible solution:

```py
def dequeue(self):
    if self.front != self.back:
        del self.storage[self.front]
        self.front += 1
```

## `get_quantity`

What are the behaviour we wanna test?

- empty queue > 0
- otherwise returns length of queue
- does it change when dequeue is used?

Example:

```py
    def test_returns_queue_size(self):
        test_queue = Queue()
        assert test_queue.get_quantity() == 0

        test_queue.enqueue('apple')
        test_queue.enqueue('apple')
        assert test_queue.get_quantity() == 2
```

Possible Solution:

```py
def get_quantity(self):
    return self.back-self.front
```

## `is_empty`

What are the behaviour we wanna test?

- True
- False

Example:

```py
    def test_empty_queue_is_True(self):
        test_queue = Queue()

        assert test_queue.is_empty() is True

    def test_not_empty_queue_is_False(self):
        test_queue = Queue()
        test_queue.enqueue('apple')

        assert test_queue.is_empty() is False
```

```py
def is_empty(self):
    return self.get_quantity() == 0
```

**AT THIS POINT WE CAN START REFACTORING TO USE UTILITY METHODS**

## `is_full`

What are the behaviour we wanna test?

- True when full
- False when not full
- False when empty

Example:

```py
    def test_full_queue_is_True(self):
        test_queue = Queue(max_size=2)
        test_queue.enqueue('apple')
        test_queue.enqueue('apple')

        assert test_queue.is_full() is True

    def test_empty_queue_is_False(self):
        test_queue = Queue()

        assert test_queue.is_full() is False

    def test_not_full_queue_is_False(self):
        test_queue = Queue()
        test_queue.enqueue('apple')
        test_queue.enqueue('orange')
        assert test_queue.is_full() is False
```

Possible Solution:

```py
def is_full(self):
    return self.max_size == self.get_quantity()
```
