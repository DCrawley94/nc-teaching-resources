from src.move_to_manchester import move_to_manchester


def test_returns_an_empty_list_when_passed_an_empty_list():
    people = []
    expected = []

    result = move_to_manchester(people)
    
    assert result == expected

def test_single_person_location_is_updated():
    people = [{ "name": 'Simon', "age": 21, "location": 'Leeds' }]
    expected = [{ "name": 'Simon', "age": 21, "location": 'Manchester' }]

    result = move_to_manchester(people)

    assert result == expected

def test_multiple_people_location_changed():
    people = [
		{ "name": 'Mick', "age": 21, "location": 'Liverpool-ish' },
		{ "name": 'August', "age": 21, "location": 'Ancoats' },
        { "name": 'Chon', "age": 21, "location": 'Nottingham' }
    ]

    expected = [
		{ "name": 'Mick', "age": 21, "location": 'Manchester' },
		{ "name": 'August', "age": 21, "location": 'Manchester' },
		{ "name": 'Chon', "age": 21, "location": 'Manchester' }
    ]

    result = move_to_manchester(people)

    assert result == expected

def test_does_not_mutate_input():
    people = [
		{ "name": 'Mick', "age": 21, "location": 'Liverpool-ish' },
		{ "name": 'August', "age": 21, "location": 'Ancoats' },
        { "name": 'Chon', "age": 21, "location": 'Nottingham' }
    ]

    result = move_to_manchester(people)

    # Check for mutation
    assert people == [
		{ "name": 'Mick', "age": 21, "location": 'Liverpool-ish' },
		{ "name": 'August', "age": 21, "location": 'Ancoats' },
        { "name": 'Chon', "age": 21, "location": 'Nottingham' }
    ]

    # Check the reference
    assert result is not people