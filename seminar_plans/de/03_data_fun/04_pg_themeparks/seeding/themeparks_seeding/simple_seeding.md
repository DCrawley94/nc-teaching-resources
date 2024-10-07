# Temporary: Last minute Seminar change of plan

Start with Poonams previous files:

```py
# connection.py
conn = pg8000.native.Connection('danika', database="nc_games")
```

```py
# seed.py

def seed(conn, games, reviews):
    # Drop tables
    db.run('DROP TABLE IF EXISTS reviews;')
    db.run('DROP TABLE IF EXISTS games;')

    # Initial creation of table pre-done
    '''
        DROP

        CREATE

        INSERT
    '''
```

# Refresh memories on the connection file

Point out that as I'm on Mac I don't actually need to include my password in the Connection parameters but I'm doing it for demonstration purposes.

Show how I can use it by passing a command line argument:

```sh
PGPASS='password123' python db/connection.py
```

This runs fine > no errors from pg8000 which means we're in the clear.

If I wanted to I could make use of the python-dotenv library instead:

```py
# in connection.py

from dotenv import load_dotenv

load_dotenv()
```

**Both are valid, the dotenv approach is a bit nicer as we don't need to rely on a bunch of command line arguments**

To run the seed function run this command:

```sh
python db/run-seed.py
```

Point out the module not found error. Ask students to think back to where we've seen this before and think about how we fixed it.

**Spoiler the import statement is fine**

Hopefully students lead us to PYTHONPATH:

```sh
PYTHONPATH=$(pwd) python db/run-seed.py
```

## DB structure

Show image with DB structure - we can see two tables, one has a foreign key that relies on the games table.

Therefore that will need to be the first we create (and also insert data when we get to that part)

## Table creation

Table creation is already done - **Ask students why it was done in this order**

```python
conn.run("""
    CREATE TABLE reviews (
        review_id SERIAL PRIMARY KEY,
        game_id INT REFERENCES games(game_id) NOT NULL,
        username VARCHAR(50) NOT NULL,
        comment VARCHAR NOT NULL,
        rating INT NOT NULL
    );
    """)

```

## Inserting games data

Take the time to look at the data that needs to be inserted.

Point out that we have all the columns needed to populate the games table.

Point out that we have access to the games data in the params - ask someone to help pseudocode out an approach to inserting the games data.

Hopefully this will lead towards using a for loop for insertion, get some help building the functionality up to something like this:

```py
for game in games:
    insert_query = f"""
    INSERT INTO games
    (game_title, release_year, console_name, image_url)
    VALUES
    (:game_title, :release_year, :console_name, :image_url);
    """
    conn.run(insert_query, **game)
```

Ask students their opinions on this solution - could it be improved?

- currently it is looping through and running an insert for every single row > it would be nicer to insert many rows at once like we've seen in SQL scripts
- How might we do something like that?

## Inserting reviews data

Ask students to think about what we have and what we need to do.

**Can they foresee a problem if we were to insert the reviews data as is?**

**Ask them to think on how we might tackle this problem**

**Ask students for help in pseudocoding out a bit of a solution at a high level**

Example:

```py
# Take existing games data and raw review data
# add game_id property to each review
# this game id comes from inserted game data
# delete existing game_title property
```

Explain that this is some reasonably complex logic and as such we should extract it out into it's own function. This will then enable us to use TDD to ensure that this logic as working as it should.

❗ _Highlight that this is an example of the relevance of testing in a larger context._

❗ _We can isolate a unit of code and test it in isolation._

❗ _This gives us increased confidence in our code and should enable us to iron out any possible bugs._

Ask students to think about how they might deal with this problem:

- We need some way of accessing the game ID from the inserted data

- > Is there anything in the raw reviews data that we could use to link to the game_id

**game_title** is in both!

- We can make use of the game title in some way - we could make use of some reasonably complex logic to find the list with the correct game_title and use that to find the game_id but there might be an easier way.

- We're going to make use of what's known as a lookup object/reference object.

## Reviews Insertion solution

```py
def insert_games(conn, games):
    """Should insert games data into the games table"""
    inserted_games = []

    for game in games:
        insert_query = """
        INSERT INTO games
        (game_title, release_year, console_name, image_url)
        VALUES
        (:game_title, :release_year, :console_name, :image_url)
        RETURNING *;
        """
        game = conn.run(insert_query, **game)
        inserted_games.extend(game)

    return inserted_games


def format_reviews(inserted_games, reviews):
    title_id_lookup = {game[1]: game[0] for game in inserted_games}
    for review in reviews:
        review["game_id"] = title_id_lookup.get(review["game_title"])
        del review["game_title"]

    return reviews


def insert_reviews(conn, reviews):
    for review in reviews:
        insert_query = """
        INSERT INTO reviews
        (game_id, username, comment, rating)
        VALUES
        (:game_id, :username, :comment, :rating);
        """
        conn.run(insert_query, **review)
```

Explain that as this is some functionality that's not tied to the SQL inserts I'm going to create a util function so it's nice and testable.

First let's look at creating a lookup object.

Possible solution:

```py
def create_games_lookup(inserted_games):
    """
    Should accept nested list of games and return dictionary
        containing game title and game id
    """
    return {game[1]: game[0] for game in inserted_games}
```

### Lookup Object: passed empty list

```py
def test_create_games_lookup_empty_list():
    assert create_games_lookup([]) == {}
```

### Lookup Object: passed single nested list

```py
def test_create_games_lookup_single_game():
    test_games_input = [[1, 'Mario Kart 64', 1996, 'N64', 'test_url.jpg']]

    assert create_games_lookup(test_games_input) == {'Mario Kart 64': 1}
```

### Lookup Object: passed multiple nested list

```py
def test_create_games_lookup_multiple_games():
    test_games_input = [
        [1, 'Mario Kart 64', 1996, 'N64', 'test_url.jpg'],
        [2, 'Donkey Kong', 1983, 'NES', 'test_url.jpg'],
        [3, 'Mario Bros', 1985, 'NES', 'test_url.jpg']
    ]
    assert create_games_lookup(test_games_input) == {'Mario Kart 64': 1, 'Donkey Kong': 2, 'Mario Bros': 3}
```

## Format Review Code

Before starting this take a moment to remind them what the data currently looks like - explain that I'm not gonna mess around with the structure of the data but rather just update the dictionaries to have IDs rather than game titles. Once that's done it can be inserted in the same manner that we did previously.

Possible solution:

```py
def format_reviews(raw_reviews, games_id_lookup):
    """
    Accepts raw reviews data as a list of dictionaries and should
        replace game title with appropriate game_id in each dictionary.
    """
    raw_reviews_copy = deepcopy(raw_reviews)

    for review in raw_reviews_copy:
        review['game_id'] = games_id_lookup[review['game_title']]
        del review['game_title']

    return raw_reviews_copy
```

### Format Reviews: Empty list

```py
def test_format_reviews_empty_list():
    assert format_reviews([], {}) == []
```

### Format Reviews: Single review

```py
def test_format_reviews_single_review():
    input_reviews = [
        {
            "username": "fola",
            "game_title": "Mario Kart 64",
            "comment": "Comment comment comment",
            "rating": 5
	    }
    ]
    input_lookup = {
        "Mario Kart 64": 1
    }

    expected = [
        {
            "username": "fola",
            "game_id": 1,
            "comment": "Comment comment comment",
            "rating": 5
	    }
    ]

    assert format_reviews(input_reviews, input_lookup) == expected
```

### Format Reviews: Multi reviews

```py
def test_format_reviews_multi_reviews():
    input_reviews = [
        {
            "username": "fola",
            "game_title": "Mario Kart 64",
            "comment": "Comment comment comment",
            "rating": 5
	    },
        {
            "username": "rogersop",
            "game_title": "Donkey Kong",
            "comment": "another comment",
            "rating": 4
	    }
    ]
    input_lookup = {
        "Mario Kart 64": 1,
        "Donkey Kong": 2
    }

    expected = [
        {
            "username": "fola",
            "game_id": 1,
            "comment": "Comment comment comment",
            "rating": 5
	    },
        {
            "username": "rogersop",
            "game_id": 2,
            "comment": "another comment",
            "rating": 4
	    }
    ]

    assert format_reviews(input_reviews, input_lookup) == expected
```

### MUTATION TESTS

**Can talk about tests for mutation here**

## Final data insertion:

```py
inserted_games = conn.run('SELECT * FROM games;')

# Create games_id lookup for formatting reviews
games_id_lookup = create_games_lookup(inserted_games)

# Format them to get game_id instead of game_title
formatted_reviews = format_reviews(reviews, games_id_lookup)

# insert prepared reviews data - another horrible for loop
for review in formatted_reviews:
    insert_query = f"""
    INSERT INTO reviews
    (game_id, username, comment, rating)
    VALUES
    (:game_id, :username, :comment, :rating)
    """

    conn.run(insert_query, **review)
```
