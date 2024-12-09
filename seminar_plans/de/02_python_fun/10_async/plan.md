# asyncio overview

## Learning Objectives

- Know how to work with asynchronous Python code
- Be able to manage concurrent asynchronous calls using the asyncio library

## Introduction - Figjam

Introduce my asynchronous function on Figjam - explain that the asynchronicity is very forced but it is used to represent a blocking task such as file read/write operations and http requests.

## Task 1: single asynchronous request

Pick on someone to talk me through the initial creation of the function:

Things to query:

- why do we need the function to be async?
- how do we get the result from the dice_roll function?

Solution:

```py
async def roll_single_dice():
    result = await dice_roll()

    return {"dice_roll": result}
```

## Task 2:

Introduce the second task and pick on people to help with the solution.

Things to ask:

- default args
- do we _need_ `gather` for the first two tests?

Working through the tests:

```py
# 1

async def roll_multiple_dice():
    result = await dice_roll()

    return {"dice_rolls": [result]}
```

**Can do this to pass second test before needing gather**

```py
# 2

async def roll_multiple_dice(rolls=1):
    dice_results = [await dice_roll() for _ in range(rolls)]
    # dice_results = await asyncio.gather(*[dice_roll() for _ in range(rolls)])
    return {"dice_rolls": dice_results}
```

```py
# 3

async def roll_multiple_dice(rolls=1):
    dice_results = await asyncio.gather(*[dice_roll() for _ in range(rolls)])
    return {"dice_rolls": dice_results}
```
