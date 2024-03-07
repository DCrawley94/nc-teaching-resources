# Fix the function below to pass the test!

def shopping_trip(money, item):
    items_and_prices = {
        "Danika's tears": 10,
        "Alex's soul": 3,
        "Simon's beard": 67,
        "Kyle's house": 49,
        "Chon's glasses": 23
    }
    if money <= items_and_prices[item]:
        return f"You can buy {item}!"

    return f"You can't afford {item}..."
