from src.dice_rollers import roll_single_dice, roll_multiple_dice
from time import time
import pytest


class TestRollSingleDice:
    @pytest.mark.asyncio
    async def test_roll_single_dice_returns_result_of_single_roll(self):
        result = await roll_single_dice()

        assert result["dice_roll"] in range(1, 7)


class TestRollMultipleDice:
    @pytest.mark.asyncio
    async def test_roll_multiple_dice_default_single_dice_roll(self):
        result = await roll_multiple_dice()
        dice_rolls = result["dice_rolls"]

        assert len(dice_rolls) == 1
        assert dice_rolls[0] in range(1, 7)

    @pytest.mark.asyncio
    async def test_roll_multiple_dice_rolls(self):
        result = await roll_multiple_dice(3)
        dice_rolls = result["dice_rolls"]

        assert len(dice_rolls) == 3
        assert all([roll in range(1, 7) for roll in dice_rolls])

    @pytest.mark.asyncio
    async def test_roll_multiple_dice_concurrent_rolls(self):
        start_time = time()
        await roll_multiple_dice(5)
        execution_time = time() - start_time

        assert execution_time < 4
