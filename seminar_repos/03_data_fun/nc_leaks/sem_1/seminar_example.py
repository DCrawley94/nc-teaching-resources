import requests
import json


def get_film_data(film_id):
    """gets data for given film_id and saves character data in a local file"""
    pass


def get_character_names():
    """
    Gets character data for all urls stored in the local characters files
    and stores the names in a local JSON file
    """
    with open("./star_wars_data/films.json", encoding="utf8") as f:
        file_contents = f.read()
        character_urls = json.loads(file_contents)["characters"]

    character_data = [requests.get(url).json() for url in character_urls]

    character_info = [character["name"] for character in character_data]

    with open("./star_wars_data/character_names.json", "w", encoding="utf8") as f:
        f.write(json.dumps(character_info, indent=4))


if __name__ == "__main__":
    get_film_data(1)
    get_character_names()
