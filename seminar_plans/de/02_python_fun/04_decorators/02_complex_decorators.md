# Complex Decorators

Figjam: https://www.figma.com/board/SOoHP6xMDUnLeX0hjyMtle/Decorators-2?node-id=0-1&t=H1vJ0AKsSi0YYOlR-1

## Learning Objectives

- Know how we can customise decorators with parameters.
- Know how to build a decorator with TDD

## Introduction

Talk through how a simple decorator works.

**Make it very clear that the decorator func is invoked with a wrapped func**

Ask students if they know how it works for a decorator with arguments

**Again be very clear about how the decorated func is first invoked with the arg - then the function returned is invoked with the decorated func**

## Plan

TDD of `multiply`:

Start by asking questions about what are the characteristics of this decorator that we can test:

- what should the decorator return? - should return a function
- what should the returned function return? - again another function
- what should this final function do? - return the result of the decorated function

- at this point highlight that the decorated function could take arguments, how do we handle that? - `*args`

### Test decorator returns a function

```py
def test_multiply_returns_a_function():
    result = multiply(3)
    assert callable(result)
```

Solution:

```py
def multiply(num):
    def outer_wrapper():
        pass

    return outer_wrapper
```

### Test returned func returns a func

```py
def test_returned_func_returns_second_func():
    def quick_maths():
        return 2 + 2 - 1

    result = multiply(2)(quick_maths)

    assert callable(result)

```

Solution:

```py
def multiply(num):
    def outer_wrapper(func):
        def inner_wrapper():
            pass

        return inner_wrapper

    return outer_wrapper
```

### Test multiply calls decorated function

**State that at this point I'm confident enough to use the decorator as intended - makes test clearer about the function intended use case**

```py
def test_multiply_wrapper_calls_given_function_once():
    has_been_called = False

    @multiply(5)
    def test_func():
        nonlocal has_been_called
        has_been_called = True
        return 0

    test_func()

    assert has_been_called
```

Solution:

```py
def multiply(num):
    def outer_wrapper(func):
        def inner_wrapper():
            func()

        return inner_wrapper

    return outer_wrapper
```

### Test multiply returns result of func multiplied by given number

```py
def test_multiply_returns_the_multiplied_result():
    @multiply(2)
    def quick_maths():
        return 2 + 2 - 1

    result_1 = quick_maths()

    assert result_1 == 6
```

**Ask students if this test gives them enough confidence - can always include a second assert to make sure**

Solution:

```py
def multiply(num):
    def outer_wrapper(func):
        def inner_wrapper():
            return num * func()

        return inner_wrapper

    return outer_wrapper
```

### Test returned function can accept args

```py
def test_multiply_invokes_given_function_when_function_accepts_args():
    passed_args = None

    @multiply(2)
    def mock_func(arg_1, arg_2):
        nonlocal passed_args
        passed_args = [arg_1, arg_2]
        return arg_1 + arg_2

    mock_func(1, 2)

    assert passed_args == [1, 2]
```

Solution:

```py
def multiply(num):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            return num * func(*args)

        return inner_wrapper

    return outer_wrapper
```

**AT THIS POINT COULD ALSO HIGHLIGHT KWARGS**

---

Final Solution:

```py
def multiply(num):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            return num * func(*args)

        return inner_wrapper

    return outer_wrapper
```
