# Requests Seminar

## Learning Objectives:

- Know how to make GET requests to an API
- Be able to access needed data from the response object
- Utilise our knowledge of file io to save and work with data locally

Figjam: https://www.figma.com/board/qpkjWwy8n7cVYM370X8g3g/Requests-Seminar?node-id=0-1&t=uHinKeZowW4o5vGa-1

- https://swapi.dev/documentation
-

## Task 2 - `get_film_data`

**For this task we will be making use of the Star Wars API**

Introduce the first task we're going to be doing:

Writing a function that accepts a film id and queries the Star Wars API for data about the specified film. This film is then saved in local JSON file.

For example:

```py
get_film_data(1)

# Queries for data about the first film and writes it to a file contained within the `star_wars_data` directory
```

Possible solution:

```py
def get_film_data(film_id):
    """gets data for given film_id and saves character data in a local file"""
    response = requests.get(f"https://swapi.dev/api/films/{film_id}")
    film_data = response.text

    with open('./star_wars_data/films.json', 'w', encoding='utf8') as f:
        f.write(film_data)
        # This will create a JSON file that is 1 long line
        # Optionally you can show the use of json.loads to format the JSON as
        #   shown in the function below
```

Break down the problem into steps and pick on students to help write it:

- what's the first thing we need to do? - create request
- how do we control which film_id were using? - f string
- How do we access the data on the response object? - `json()` or `text`
- How do we write to a file? What is the with block? - with context manager
- Do we need any extra configuration for opening the file for write operations - `w` (can leave this and debug the UnsupportedOperation error with them)

If using `.json()` explore why this isn't working (Incorrectly converting python dictionary to JSON string - use JSON library instead or just `.text` attribute as it's already JSON)

## Task 2 - `get_character_names`

- Create a new function named `get_character_names`
- This function should make use of the character urls in the data fetched by the first function to access data about each character.
- The names of each character should be saved to a local file

For example:

```py
get_film_data(1)
get_character_data()

# The function `get_character_data` queries the star wars API for data about all the characters in the first film
# It creates a JSON file containing a list of the characters names, for example
```

```json
[
  "Luke Skywalker",
  "C-3PO",
  "R2-D2",
  ...
]
```

Possible Solution:

```py
def get_character_names():
    """
    Gets character data for all urls stored in the local characters files
    and stores the names in a local JSON file
    """
    with open('./star_wars_data/films.json', encoding='utf8') as f:
        file_contents = f.read()
        character_urls = json.loads(file_contents)['characters']

    character_data = [requests.get(url).json() for url in character_urls]

    character_info = [character['name'] for character in character_data]

    with open(
        './star_wars_data/character_names.json', 'w', encoding='utf8') as f:
        f.write(json.dumps(character_info, indent=4))
```

Break down the problem into steps and pick on students to help write it:

- what's the first thing we need to do? - access file data
- how? - `open` - can do `r` flag but I think it defaults to read
  **LOOK AT DOCS FOR INFO ON REQUEST RESPONSE**
- then what? Find character URLS and make a request for each one, convert each one to JSON
- then with the list of JSON data we just need to filter down to the character name and save the final list of names to a file.

**Round it off by talking about improvements we could make - lots of synchronous blocking requests - use `aiohttp` instead**

https://docs.aiohttp.org/en/stable/

**FINALLY: CHECK IF ANYONE HAS MADE A HELPDESK**

Go over first task getting instructions
