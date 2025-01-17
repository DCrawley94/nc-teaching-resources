import requests
import json
from pprint import pprint


def get_film_data(film_id):
    """gets data for given film_id and saves film data in a local file"""

    # GET request
    # F string insert the film_id into the url
    url = f"https://swapi.dev/api/films/{film_id}"
    # Access data from the response
    response_body = requests.get(url).json()

    # Save as a JSON file
    with open("star_wars_data/film.json", "w", encoding="utf8") as file:
        json.dump(response_body, file, indent=4)


def get_character_names():
    """
    Gets character data for all urls stored in the local films.json file
    and stores *just* their names in a local JSON file.
    """

    # Read previously created file
    with open("star_wars_data/film.json", "r") as file:
        # Access character list
        character_urls = json.load(file)["characters"]

    # char_names = []
    # # Iterate through character and make GET request for each one
    # for url in character_urls:
    #     res = requests.get(url)
    #     # Convert response body to usable Python dictionary
    #     char_name = res.json()["name"]

    #     # Append the names from each response to a list
    #     char_names.append(char_name)

    # Iterate through character and make GET request for each one
    # Convert response body to usable Python dictionary
    # Append the names from each response to a list
    char_names = [requests.get(url).json()["name"] for url in character_urls]

    # Save list to new local file
    with open("star_wars_data/char_names.json", "w", encoding="utf8") as f:
        json.dump(char_names, f, indent=4)


if __name__ == "__main__":
    get_film_data(6)
    get_character_names()
