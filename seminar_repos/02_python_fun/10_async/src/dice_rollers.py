from src.dice import dice_roll
import asyncio


"""
Create a function roll_single_dice.

It should make use of of the asynchronous dice_roll function and return the
result in a dictionary like so: 

{
    "dice_roll": result
}
"""

# Task 1


async def roll_single_dice():
    result = await dice_roll()

    return {"dice_roll": result}


"""
Create a function roll_multiple_dice.

Arguments:
    *OPTIONAL* rolls - the number of dice rols to make

It should make use of of the asynchronous dice_roll function and return the
results in a dictionary like so: 

{
    "dice_rolls": [result_1, result_2, ...]
}
"""


async def roll_multiple_dice(rolls=1):
    roll_list = [dice_roll() for _ in range(rolls)]

    results = await asyncio.gather(*roll_list)

    dice_data = {"dice_rolls": results}

    return dice_data


if __name__ == "__main__":
    results = asyncio.run(roll_multiple_dice(5))

    print(results)
