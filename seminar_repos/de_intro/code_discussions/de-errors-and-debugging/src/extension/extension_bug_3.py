# Fix the function below to pass the tests!

def capital_authors(list):
    authors = []

    for pair in list:
        authors.append(pair.split("-"))

    return authors
