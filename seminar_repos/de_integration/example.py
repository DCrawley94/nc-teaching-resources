from random import randint


def load_data():
    return randint(10, 100)


def process_data():
    data = load_data()
    return data + 7
