import random
import asyncio


async def dice_roll():
    await asyncio.sleep(random.randint(1, 3))

    return random.randint(1, 6)
