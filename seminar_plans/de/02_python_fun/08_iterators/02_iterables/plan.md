Figjam: https://www.figma.com/board/jo0mMFVZ9swiQ34dPjqbfn/Iterables?node-id=0-1&t=GFSy1Uf5uwbzmLZ0-1

## Learning Objectives:

- Know how to implement the **iterator protocol** using the correct magic methods
- Use TDD to implement an Iterable class that allows for multiple iterations

## Refresher:

What is an iterator:

```txt
An object that allows you to iterate over collections of data.
```

What are the classes needed for an object to implement the iterator protocol:

```txt
> `.__iter__()` : Called to initialize the iterator. It must return an iterator object.
> `.__next__()` : Called to iterate over the iterator. It must return the next value in the data stream.
```

What is the difference between an iterable and an iterator?

```txt
**Iterable**:
Reusable
Iter returns an iterator
Next is not implemented

**Iterator**:
Single use
Implements iter/next
Iter usually returns self (an iterator)
```

```txt
According to this internal structure, you can conclude that all iterators are iterables because they meet the iterable protocol. However, not all iterables are iterators—only those implementing the .__next__() method.
```

## Introduce the problem

Creating an iterable that will allow us to loop over a collection in reverse order:

```py
# Example

backwards_list = Reversed([1,2,3])

backwards_iterator = iter(backwards_list)
next(backwards_iterator) # 3
next(backwards_iterator) # 2
next(backwards_iterator) # 1
```

Remind them that an **Iterable** does not support the next method, however it has a `__iter__` method that returns an **Iterator** which does.

---

Refresh students on how a for loop works:

- invokes `__iter__` on the object to get an iterator
- calls next on the produced iterator to iterate through
- loop stops when a StopIteration exception is raised

---

Explain that in order to achieve our goal we will be implementing two classes - an **Iterable** and an **Iterator**, we will start with the Iterator

## Iterator TDD

Starting from a half-baked implementation that only returns the final element complete to implementation of the `iterator` with two additional tests:

```py
    @pytest.mark.it(
        'Subsequent invocations of next should return elements in reverse order')
    def test_reversed_iterator_next_subsequent_invocations(self):
        test_reverse_iterator = ReversedIterator([1,2,3])
        assert next(test_reverse_iterator) == 3
        assert next(test_reverse_iterator) == 2
        assert next(test_reverse_iterator) == 1


    @pytest.mark.it(
        'StopIteration exception is raised after collection elements exhausted')
    def test_reversed_iterator_stop_iteration_raised(self):
        test_reverse_iterator = ReversedIterator([1,2,3])
        for _ in range(3):
            next(test_reverse_iterator)

        with pytest.raises(StopIteration):
            next(test_reverse_iterator)
```

Possible solution:

```py
    def __next__(self):
        if self._index < 0:
            raise StopIteration
        # This will still work due to negative indexing - needs the above condition
        value = self.collection[self._index]
        self._index -= 1
        return value
```

## Iterable Implementation

Demonstrate with repl/test file how the Iterator class can be used in a loop.

**Highlight that is a single use object - once we've iterated once that's it**

Time to create the iterable!

Ask students to think about what we might need to implement:

- Init method - we need some way of accessing the collection
- iter method:
  - What should this do?
  - How can we test it?

With student help work towards the solutions for the tests below:

```py
class TestReversedIterable:
    @pytest.mark.it('Stores given collection as an attribute')
    def test_reversed_iterable_attributes(self):
        test_reverse_iterable = ReversedIterable([1,2,3])
        assert test_reverse_iterable.collection == [1,2,3]

    @pytest.mark.it('Iter returns instance of Iterator class')
    def test_reversed_iterable_iter_returns_iterator(self):
        test_reverse_iterable = ReversedIterable([1,2,3])

        test_iterator = iter(test_reverse_iterable)

        assert isinstance(test_iterator, ReversedIterator)

    @pytest.mark.it(
        'Multiple invocations of Iter should return different iterator instances')
    def test_reversed_iterable_iter_multi_instances(self):
        test_reverse_iterable = ReversedIterable([1,2,3])

        test_iterator_1 = iter(test_reverse_iterable)
        test_iterator_2 = iter(test_reverse_iterable)

        assert test_iterator_1 is not test_iterator_2
```

Solution:

```py
class ReversedIterable:
    def __init__(self, collection):
        self.collection = collection

    def __iter__(self):
        return ReversedIterator(self.collection)
```

**Force final test to fail by creating iterator in init?**
