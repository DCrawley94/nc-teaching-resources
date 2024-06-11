from copy import deepcopy, copy
'''
correct_language takes a list of dictionary profiles
and returns a new list of profiles where each "language" value is changed to
"Python".
If the language is already "Python" no change occurs.
The original dictionary should not be mutated.
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
'''


def correct_language(profiles):
    new_profiles = deepcopy(profiles)
    for profile in new_profiles:
        profile["language"] = "Python"
    return new_profiles