# pg8000: Data Manipulation and Insertion

## Learning Objectives

- Be to identify when data needs to be manipulated before inserted into a database
- Know how to isolate a unit of logic in the seed function and test it

## Resources:

- seed function pre-written to insert games data
- DB Diagram showing DB structure - use a screenshot in repo
- example data ready for insertion

## Intro

Introduce repo. Make sure to showcase:

- connection file
- run-seed
- seed file
- ERD diagram
- Raw data

## DB structure

Show image with DB structure - we can see two tables, one has a foreign key that relies on the games table.

Therefore that will need to be the first we create (and also insert data when we get to that part)

Ask students to think about what we have and what we need to do.

**Can they foresee a problem if we were to insert the reviews data as is?**

**Ask them to think on how we might tackle this problem**

**Ask students for help in pseudocoding out a bit of a solution at a high level**

Example:

```txt

# Take existing games data and raw review data

# Use previously inserted games data to link game_title to game_id

# insert reviews data with game_id instead of game_title

```

That sounds like we're going to need a bit of data manipulation before we can insert the data.

To do this I think I'm going to create a data structure that allows me to access the `game_id` if I know the matching `game_title`.

> Can anyone think of an appropriate data type for this?

## Planning Approach

For that reason we're going to extract that aspect of the logic and test it.

❗ _Highlight that this is an example of the relevance of testing in a larger context._

❗ _We can isolate a unit of code and test it in isolation._

❗ _This gives us increased confidence in our code and should enable us to iron out any possible bugs._

In reality we should rely on a mixture of testing approaches. Unit tests only form part of that. Integration Testing will be discussed later in the week.

## Lookup Object

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

## Update Seed Function

We can now include something like this:

```py
...
# access to the inserted game data (game_id)
games_data = conn.run("SELECT game_title, game_id FROM games;")

# - some way to link game_title (review data)
# to the game_id in inserted games
game_id_lookup = {game[0]: game[1] for game in games_data}

# - when inserting reviews - we can replace title with appropriate id
insert_reviews(conn, reviews, game_id_lookup)
...
```

Insert Reviews:

```py
def insert_reviews(conn, reviews, game_id_lookup):
    insert_str = """
    INSERT INTO reviews
    (game_id, username, comment, rating)
    VALUES
    (:game_id, :username, :comment, :rating);
    """

    for review in reviews:
        game_id = game_id_lookup[review["game_title"]]
        username = review["username"]
        comment = review["comment"]
        rating = review["rating"]

        conn.run(
            insert_str,
            game_id=game_id,
            username=username,
            comment=comment,
            rating=rating,
        )
```

## Query Builder

> Ask students if they can see anything inefficiencies in the function we've created - can remind them to think about how it's done in raw SQL if necessary

> How could this be addressed?

✨ New Util Function ✨

Work with them to pseudocode how that could be done.
