# asyncio overview

## Learning Objectives

- Know how to work with asynchronous Python code
- Be able to manage concurrent asynchronous calls using the asyncio library

## Introduction - Figjam

Introduce my asynchronous function on Figjam - explain that the asynchronicity is very forced but it is used to represent a blocking task such as file read/write operations and http requests.

**Can do this to pass second test before needing gather**

```py
async def roll_multiple_dice(rolls=1):
    dice_results = [await dice_roll() for _ in range(rolls)]
    # dice_results = await asyncio.gather(*[dice_roll() for _ in range(rolls)])
    return {"dice_rolls": dice_results}

```
