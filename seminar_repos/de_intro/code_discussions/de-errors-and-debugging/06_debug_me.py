from test_api.checks import run_test, format_err_msg


#  Fix the function below to pass the test!


def add_to_list(todo):
    todos = ['Eat a hearty breakfast', 'Enjoy some art',
             'Chase a flamingo', 'Throw a bagel']
    todos.append(todos)
    return todos


@run_test
def test_returns_correct_list_values():
    addition = 'Just have a top notch day'
    expected = [
        'Eat a hearty breakfast',
        'Enjoy some art',
        'Chase a flamingo',
        'Throw a bagel',
        'Just have a top notch day'
    ]
    result = add_to_list(addition)
    assert result == expected, format_err_msg(expected, result)


if __name__ == '__main__':
    test_returns_correct_list_values()
