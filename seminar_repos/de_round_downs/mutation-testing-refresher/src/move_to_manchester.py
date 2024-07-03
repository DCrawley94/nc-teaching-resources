# This function should accept a list of dictionaries each representing a person
# e.g. [{"name": "Geoff", "age": 21, "location": "London"}, ...]
# The function should update the location property to be "Manchester"
# The new list should then be returned
# This function should not mutate the original list of people
from copy import deepcopy

def move_to_manchester(people):
    new_people = deepcopy(people)

    for person in new_people:
        person['location'] = 'Manchester'
   
    return new_people


     # people = [{**person, 'location': 'Manchester'} for person in people]