# Fix the function below to pass the test!

def super_flyers(heroes):
    known_flying_heroes = []

    for hero in heroes:
        if hero["ability"] == "flying" or hero["isAnonymous"]:
            known_flying_heroes.append(hero)

    return known_flying_heroes
