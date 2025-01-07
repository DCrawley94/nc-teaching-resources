# Iterator Seminar

## Learning Objectives:

- Know how to implement the **iterator protocol** using the correct magic methods
- Use TDD to implement an Iterator from scratch

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
Iter usually returns self
```

```txt
According to this internal structure, you can conclude that all iterators are iterables because they meet the iterable protocol. However, not all iterables are iterators—only those implementing the .__next__() method.
```

## Introduce problem:

Show documentation for [itertools.repeat](https://docs.python.org/3/library/itertools.html#itertools.repeat) ? - involved a `yield` so maybe summarise instead

`Repeat`:

- Used to create an iterator that returns the given `object` over and over.
- Runs indefinitely unless the `times` argument is specified

Show how `itertools.repeat` is used in the repl:

```sh
>>> import itertools
>>> r1 = itertools.repeat(5)
```

Show that it has an `__iter__` method that returns itself:

```sh
>>> iter(r1)
repeat(5)
>>> iter(r1) is r1
True
```

And a `__next__` method that returns the given object. As we haven't specified an argument for `times` the given object will be returned indefinitely.

```sh
>>> next(r1)
5
>>> next(r1)
5
>>> next(r1)
5
>>> next(r1)
5
>>> next(r1)
5
```

If we were to specify and argument for times then the object will be returned the set number of times when `__next__` is invoked - once the limit is reached is will raise a StopIteration error.

```sh
>>> r2 = itertools.repeat('hello', times=3)
>>> next(r2)
'hello'
>>> next(r2)
'hello'
>>> next(r2)
'hello'
>>> next(r2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

Our task is to create a custom class that re-implements this behaviour.

## Pseudocode:

Have the skeleton of a class ready to go:

```py
class Repeat:
    def __init__(self, repeat_obj, times):
      pass
```

Explain that I'm going to do a bit of pseudocode planning before jumping into implementation.

Target particular students to tell me what my class needs in order to implement the iterator protocol:

- `iter`
- `next`

What attribute (if any) might we need to assign in the initialisation method?

- `repeat_obj` and `times` so that they're accessible to other methods
- some students might suggest some kind of call count or way of tracking invocations - defer until later with the explanation that this is more of an implementation detail.

## Tests

Ask students to identify appropriate tests to build up the functionality of the class.

### Test 1: Type of Iterator - **WE MIGHT NOT REALLY NEED THIS TBH - IT'S IMPLIED BY THE OTHER TESTS ANYWAY**

Might not be obvious to students but mentions that this is quite a useful one as it ensures that our class has the correct methods to be an iterator.

```py
from typing import Iterator

@pytest.mark.it('Repeat instance should be an Iterator')
def test_is_iterator():
    test_repeat = Repeat({})

    assert isinstance(test_repeat, Iterator)
```

### Test 2: Attributes

```py
@pytest.mark.it('Repeat instance has the correct attributes')
def test_repeat_attributes():
    test_repeat = Repeat(5, times=3)

    assert test_repeat.repeat_obj == 5
    assert test_repeat.times == 3
```

### Test 3: Default Times Attribute

```py
@pytest.mark.it('When passed no times argument, times should default to None')
def test_repeat_default_attribute():
    test_repeat = Repeat(5)

    assert test_repeat.times == None
```

### Test 4: Iter Method returns self

**FOR THIS TEST TO WORK THERE NEEDS TO BE A NEXT METHOD IN PLACE EVEN IF IT JUST HAS PASS**

```py
@pytest.mark.it('When invoked with iter a repeat instance should return itself')
def test_iter_returns_self():
    test_repeat = Repeat(5)

    assert iter(test_repeat) is test_repeat
```

```py
def __iter__(self):
    return self
```

### Test 5: No limit > object returned indefinitely

```py
@pytest.mark.it('When no limit is set, given object should be returned indefinitely when invoked with next')
def test_repeat_returns_object_indefinitely():
    test_repeat = Repeat(5)

    for _ in range(1000):
        assert next(test_repeat) == 5
```

```py
def __next__(self):
    return self.repeat_obj
```

### Test 6: With limit > object returned set number of times before StopIteration is raised

```py
@pytest.mark.it('When a limit is set, given object should be returned no more than the given value for times')
def test_repeat_with_times():
    test_repeat = Repeat(5, times=3)

    next(test_repeat)
    next(test_repeat)
    next(test_repeat)

    with pytest.raises(StopIteration):
        next(test_repeat)
```

```py
# Solution

def __next__(self):
        if self.times:
            if self.__call_count < self.times:
                self.__call_count += 1
                return self.repeat_obj
            else:
                raise StopIteration
        return self.repeat_obj
```

## Possibly useful demo:

Ask students to remind me how a for loop works.

- iter invoked
- next invoked on the return value of iter

Lets see our iterator working with some print statements:

```py
class Repeat:
    def __init__(self, repeat_obj, times=None):
        self._repeat_obj = repeat_obj
        self._times = times
        self._call_count = 0

    def __iter__(self):
        print('__iter__ called')
        return self

    def __next__(self):
        if self._times:
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
```
