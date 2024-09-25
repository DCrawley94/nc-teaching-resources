**Can do this to pass second test before needing gather**

```py
async def roll_multiple_dice(rolls=1):
    dice_results = [await dice_roll() for _ in range(rolls)]
    # dice_results = await asyncio.gather(*[dice_roll() for _ in range(rolls)])
    return {"dice_rolls": dice_results}

```
