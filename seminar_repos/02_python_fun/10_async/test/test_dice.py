from src.dice import dice_roll
from time import time
import pytest


@pytest.mark.asyncio
async def test_dice_roll_6_sided_dice():
    result = await dice_roll()

    assert 0 < result <= 6


@pytest.mark.asyncio
async def test_dice_roll_execution_time_should_be_between_1_and_4_seconds():
    start_time = time()

    await dice_roll()

    execution_time = time() - start_time

    assert 1 < execution_time < 4
