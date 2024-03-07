# Fix the function below to pass the tests!

def clever_banking(value, interest_rate, years):
    bank_account = value

    for i in range(1, years + 1):
        bank_account += (1 + interest_rate)

    return value
