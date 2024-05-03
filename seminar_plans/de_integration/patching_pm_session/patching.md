# Patching

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

## Introduce Patch

Patch docs: https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch

Things to point out in the docs:

- can be used in multiple ways, we will look at a few of the options
- target should be a string which points to the thing we want to mock
- We should patch where an object is **used** not where it is **defined**
- even if `load_data` is in a different location we'd still patch the 'example_1' file

**Take the time to EXTRACT TO SEPARATE FILE TO DEMONSTRATE IT**

### Test 1: start and stop

Talk through the following:

- create patcher and print, show that it is a `patch` object.
- explain that currently it's not doing anything, show the dir and how it has a **start** and **stop** method.
- show how we use these methods to enable and disable the mock.
- the target is imported when the test is executed

**Before starting and stopping the patcher print it to show it's a patch object - also print `load_data` to show that it isn't mocked until we call start**

```py
def test_process_data_1():
    patcher = patch('src.example_1.load_data', return_value=8)

    patcher.start()
    assert process_data() == 15
    patcher.stop()

    # assert process_data() == 15
    # Can include this to show that patch is disabled
```

### Test 2: context manager

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
```

Highlight that the `with` context will call patcher start and stop.

**Alias the patcher and print in tests - compare this to the print of `load_data` notice it is the same - therefore we can add functionality the the mock if we desire**

### Test 3: Decorator

Explain that we could use a **decorator**.

```py
@patch('src.example_1.load_data', return_value=8)
def test_process_data_3(patch_load_data):  # Point out that for this to work we need to pass in an argument that represents the mocked `load_data` function
    assert process_data() == 15
```

The three methods of patching `load_data` are functionally the same.

**The students will likely see the decorator used a lot but they can use whichever one they prefer**

## More realistic example of `patch`:

We have a function, `get_games`, which will query the `nc_games` database. Then format the response from the database and finally return the formatted response.

This function has a dependency, what is that dependency?

- The database/ database connection

Querying the actual database isn't something I want to do for the following reasons:

- There could be hundreds of thousands of rows, this code is blocking and could take some time.
- I don't want to be testing with real data, admittedly there's not much that could go wrong with a SELECT but if I was INSERTING or UPDATING data I definitely would not want this
- The only functionality I really want to test is that the data returned from the SELECT is correctly formatted.

Therefore I can patch the connection in order to control what is returned by the `run` method.

**ask students preference between context manager and decorator - if there's time we can always do a refactor at the end**

### Test 1: Handles case of no data returned:

**start by asking students for help in creating the mock functionality - hopefully the struggle and we can work towards a solution together**

Start off by creating a mock connection class and using that and the return value:

```py
class MockConnection:
    def run(self, query):
        return []

@patch('src.example_2.Connection', return_value = MockConnection())
def test_get_games_no_data(mock_conn):
    # I can leverage the functionality of the `mock`
    # This is essentially saying that Connection will return a Mock and that Mock will have a `run` method`
    assert get_games() == []
```

❗ Refactor to **lazy attributes**!

```py
@patch('src.example_2.Connection')
def test_get_games_no_data(mock_conn):
    mock_conn().run.return_value = []
    # I can leverage the functionality of the `mock`
    # This is essentially saying that Connection will return a Mock and that Mock will have a `run` method`
    assert get_games() == []
```

### Test 2: Handle single returned row:

```py
@patch('src.example_2.Connection')
def test_get_games_single_row(mock_conn):
    mock_conn().run.return_value = [
        [1, 'Skyrim 2', 1999, 'www.website.com', 'PS2']]

    assert get_games() == [
        {
            'games_id': 1,
            'game_title': 'Skyrim 2',
            'release_year': 1999,
            'image_url': 'www.website.com',
            'console_name': 'PS2'
        }
    ]
```

### Test 3: Test error handling

```py
from pg8000.exceptions import DatabaseError

# ~~~~~

def test_get_games_handles_db_error():
    with patch('src.example_2.Connection') as mock_conn:
        mock_conn().run.side_effect = DatabaseError

        assert get_games() == 'Error querying the database'
```

### Test 4: Multiple returned rows (only if there's time)

```py
@patch('src.example_2.Connection')
def test_get_games_multi_row(mock_conn):
    mock_conn().run.return_value = [
        [1, 'game1', 1999, 'www.website.com', 'PS2'],
        [2, 'game2', 2001, 'www.website2.com', 'Xbox']]

    assert get_games() == [
        {
            'games_id': 1,
            'game_title': 'game1',
            'release_year': 1999,
            'image_url': 'www.website.com',
            'console_name': 'PS2'
        },
        {
            'games_id': 2,
            'game_title': 'game2',
            'release_year': 2001,
            'image_url': 'www.website2.com',
            'console_name': 'Xbox'
        },
    ]
```
