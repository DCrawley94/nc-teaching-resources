# Patching

Urllib??

## Learning Objectives

- Know how to use `patch` to temporarily replace a target object.
- Understand how to use `patch` for testing purposes.

## Refresher

Why do we need mocks?

- You may want to test some code that depends on other objects
- However when writing unit tests we want to test **in isolation**
- Using mocks we can simulate the behaviour of certain objects and control the necessary things in order to enable our testing

The purpose of mocking is to isolate and focus on the code being tested and not on the behaviors or state of external dependencies.

## Introduce the problem:

I want to test the `process_data` function, however it has some dependancies that are currently outside of my control.

> ❓ What does the `process_data` function depend on?

- `load_data` and in turn `randint`

The behaviour I want to test is that it correctly adds 7 to the result of the `load_data` function. Therefore I need to control `load_data`.

---

Previously we saw that we can do this via dependency injection - i.e. I could pass `load_data` in and in my tests this would be replaced with a `mock`.

Now we're going to look at a different method of mocking. We're going to use `patch`.

### Test 1: context manager

Repeat the test with a context manager:

- create patcher then use with:

```py
def test_process_data_2():
    patcher = patch('src.example_1.load_data', return_value=8)

    with patcher:
        assert process_data() == 15
```

Refactor to this:

```py
def test_process_data_2():
    with patch('src.example_1.load_data', return_value=8):
        assert process_data() == 15
    # assert process_data() == 15
    # Can include this to show that patch is disabled
```

Highlight that the `with` context will call patcher start and stop.

**Alias the patcher and print in tests - compare this to the print of `load_data` notice it is the same - therefore we can add functionality the the mock if we desire**

### Test 2: Decorator

Explain that we could use a **decorator**.

```py
@patch('src.example_1.load_data', return_value=8)
def test_process_data_3(patch_load_data):  # Point out that for this to work we need to pass in an argument that represents the mocked `load_data` function
    assert process_data() == 15
```

The three methods of patching `load_data` are functionally the same.

**The students will likely see the decorator used a lot but they can use whichever one they prefer**

## More realistic example of `patch`:

We have a function, `run_and_log`, which runs a given function and returns a log message.

This function has a dependency, what is that dependency?

- Datetime - specifically the current timestamp.

If I run this test without controlling datetime it will be different each time.

**The only functionality I really want to test is that the the log message is created and returned successfully**

Therefore I can patch datetime in order to control what is returned by the `strftime` method.

**ask students preference between context manager and decorator - if there's time we can always do a refactor at the end**

### Test 1: Handles case of function with return value:

**start by asking students for help in creating the mock functionality - hopefully the struggle and we can work towards a solution together**

Start off by creating a mock connection class and using that and the return value:

```py
class MockDateObj:
    def strftime(self, format):
        return '2024-05-09 09:57:07'

@patch('src.example_2.datetime')
def test_log_message_func_with_return_value(mock_dt):
    # I can leverage the functionality of the `mock`
    # This is essentially saying that datetime.now will return a Mock and that Mock will have a `strftime` method`
    def func_with_return():
        return 'test func response'

    mock_dt.now.return_value = MockDateObj()

    assert run_and_log(func_with_return) == (
        "2024-05-09 09:57:07 - func_with_return ran successfully: "
        "test func response")
```

❗ Refactor to **lazy attributes**!

```py
@patch("src.example_2.datetime")
def test_log_message_func_with_return_value(mock_dt):
    def func_with_return():
        return "test func response"

    mock_dt.now().strftime = Mock(return_value="2024-05-09 09:57:07")

    assert run_and_log(func_with_return) == (
        "2024-05-09 09:57:07 - func_with_return ran successfully: " "test func response"
    )
```

### Test 2: Handle no return value:

```py
@patch("src.example_2.datetime")
def test_log_message_func_with_no_return_value(mock_dt):
    def func_no_return():
        pass

    mock_dt.now().strftime = Mock(return_value="2024-05-09 09:57:07")

    assert (
        run_and_log(func_no_return)
        == "2024-05-09 09:57:07 - func_no_return ran successfully"
    )
```

### Test 3: Test error handling

**THIS IS OKAY BUT COULD MAYBE IMPROVE IT TO MAKE IT USE SIDE_EFFECT**

```py
@patch("src.example_2.datetime")
def test_log_message_function_exception(mock_dt):
    def func_raising_error():
        raise Exception("Something went wrong")

    mock_dt.now().strftime.return_value = "2024-05-09 09:57:07"

    assert run_and_log(func_raising_error) == (
        "2024-05-09 09:57:07 - func_raising_error encountered an error: "
        "Something went wrong"
    )
```
