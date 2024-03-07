# Fix the function below to pass the tests!

def sum_sentence(list):
    costs = []
    for fruit_dict in list:
        costs.append(fruit_dict['cost'])

    total = costs
    return "The total cost of the fruits is £" + str(total)
