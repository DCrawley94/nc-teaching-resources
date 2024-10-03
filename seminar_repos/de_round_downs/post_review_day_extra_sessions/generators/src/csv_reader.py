import time


def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result


def csv_reader_gen(file_name):
    for row in open(file_name, "r"):
        yield row


if __name__ == "__main__":
    csv_gen = csv_reader_gen("test/pizzas.csv")
    while True:
        time.sleep(1)
        print(next(csv_gen))
