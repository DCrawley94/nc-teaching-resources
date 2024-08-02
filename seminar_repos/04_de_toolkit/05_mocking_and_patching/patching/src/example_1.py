from src.module_1 import load_data


def process_data():
    try:
        data = load_data()
        return f"The processed data is {data + 7}"
    except ValueError:
        return "There was an error"
