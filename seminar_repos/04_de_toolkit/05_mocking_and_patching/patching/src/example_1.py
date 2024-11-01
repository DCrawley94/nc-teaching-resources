from random import randint


def load_data():
    return randint(10, 100)


def process_data():
    try:
        data = load_data()
        return f"The processed data is {data + 7}"
    except ValueError:
        return "There was an error"
