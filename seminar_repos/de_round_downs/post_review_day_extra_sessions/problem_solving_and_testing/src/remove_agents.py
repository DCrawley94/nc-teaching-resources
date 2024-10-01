"""
Your function should take a list of dictionaries representing users'
social media profiles, and remove any suspected spies.

An employee is known to be a mole if the letter mole appear in
their 'about me' description or their list of interests.
"""

from copy import deepcopy


def remove_agents(employees):
    employees_copy = deepcopy(employees)

    non_spies = []

    for employee in employees_copy:
        about_me = employee["about_me"]
        interests = employee["interests"]

        if "mole" not in about_me:
            for interest in interests:
                print(interest)
                if "mole" not in interest:
                    non_spies.append(employee)

    return non_spies


def check_interests():
    pass


def check_about_me():
    pass
