# Async Seminar

The idea for this seminar is to work through implementations of the two dice rolling functions.

You don't need to cover testing so I'd recommend having tests pre-written (with skip decorators) and work through the implementations.

For the second function it's only the final test that requires you to use `gather`. You can pass the previous tests without relying on concurrency like so:

```py
async def roll_multiple_dice(rolls=1):
    dice_results = [await dice_roll() for _ in range(rolls)]
    return {"dice_rolls": dice_results}
```

---

Just a heads up there are tests written for the provided dice_roll function so you will probably want to just run the tests in the `test_dice_rollers` during the seminar so it's not super slow.
