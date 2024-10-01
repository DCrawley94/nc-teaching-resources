from src.remove_agents import remove_agents


# empty list
def test_remove_agents_empty_list():
    assert remove_agents([]) == []


# list of non-spies
def test_remove_agents_no_spies():
    non_spies = [
        {
            "name": "Sam",
            "age": 30,
            "about_me": "I have no personality! :D",
            "interests": ["code", "guac"],
        }
    ]

    expected = [
        {
            "name": "Sam",
            "age": 30,
            "about_me": "I have no personality! :D",
            "interests": ["code", "guac"],
        }
    ]

    assert remove_agents(non_spies) == expected


# Does not mutate input
def test_remove_agents_does_not_mutate_input():
    input_employees = [
        {
            "name": "Sam",
            "age": 30,
            "about_me": "I have no personality! :D",
            "interests": ["code", "guac"],
        }
    ]

    unmutated_input = [
        {
            "name": "Sam",
            "age": 30,
            "about_me": "I have no personality! :D",
            "interests": ["code", "guac"],
        }
    ]

    assert remove_agents(input_employees) is not input_employees
    assert input_employees == unmutated_input


# with spies:


# whole word mole in about me
def test_remove_agents_whole_mole_about_me():
    input_employees = [
        {
            "name": "Sam",
            "age": 30,
            "about_me": "I have no personality! :D",
            "interests": ["code", "guac"],
        },
        {
            "name": "Mitch",
            "age": 29,
            "about_me": "I am not a mole - I am a human being!",
            "interests": ["Tudor hymns", "dancing"],
        },
    ]

    expected_output = [
        {
            "name": "Sam",
            "age": 30,
            "about_me": "I have no personality! :D",
            "interests": ["code", "guac"],
        }
    ]

    assert remove_agents(input_employees) == expected_output


# whole word mole in interests
def test_remove_agents_whole_mole_in_interests():
    input_employees = [
        {
            "name": "Sam",
            "age": 30,
            "about_me": "I have no personality! :D",
            "interests": ["code", "guac", "moles"],
        },
        {
            "name": "Mitch",
            "age": 29,
            "about_me": "I am a human being!",
            "interests": ["Tudor hymns", "dancing"],
        },
    ]

    expected_output = [
        {
            "name": "Mitch",
            "age": 29,
            "about_me": "I am a human being!",
            "interests": ["Tudor hymns", "dancing"],
        }
    ]

    assert remove_agents(input_employees) == expected_output


# word mole but separate letters in about me
# word mole but separate letters in interests

# All of the above - but ignoring case
