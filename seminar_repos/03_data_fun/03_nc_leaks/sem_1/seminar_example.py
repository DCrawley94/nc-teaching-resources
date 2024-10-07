import requests
import json


def get_film_data(film_id):
    """gets data for given film_id and saves character data in a local file"""
    film_data = requests.get(f"https://swapi.dev/api/films/{film_id}/").json()

    with open("./star_wars_data/film.json", "w", encoding="utf-8") as f:
        json.dump(film_data, f, indent=4)


def get_character_names():
    """
    Gets character data for all urls stored in the local characters files
    and stores the names in a local JSON file
    """
    with open("./star_wars_data/film.json", "r", encoding="utf-8") as f:
        character_urls = json.load(f)["characters"]

    character_names = [requests.get(url).json()["name"] for url in character_urls]

    with open("./star_wars_data/character_names.json", "w", encoding="utf-8") as f:
        json.dump(character_names, f, indent=4)


if __name__ == "__main__":
    get_film_data(3)
    get_character_names()
