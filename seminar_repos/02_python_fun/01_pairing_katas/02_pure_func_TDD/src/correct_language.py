from copy import deepcopy

"""
correct_language takes a list of dictionary profiles
and returns a new list of profiles where each "language" value is changed to
"Python".

If the language is already "Python" no change occurs.
The original list and dictionaries should not be mutated.
e.g.
correct_language([
                    { "name" : "Kyle", "language" : "Javascript" },
                    { "name" : "Liam", "language" : "Go" }
                ])

# returns
[
    { "name" : "Kyle", "language" : "Python" },
    { "name" : "Liam", "language" : "Python" }
]
"""


def correct_language(profiles):
    profiles_copy = deepcopy(profiles)
    for profile in profiles_copy:
        profile["language"] = "Python"
    return profiles_copy
