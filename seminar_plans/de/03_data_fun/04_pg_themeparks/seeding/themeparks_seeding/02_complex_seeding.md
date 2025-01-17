# pg8000: Data Formatting with TDD

## Learning Objectives

- Be to identify when data needs to be manipulated before inserted into a database
- Know how to isolate a unit of logic in the seed function and test it

## Intro

Resources:

- seed function pre-written to insert games data
- DB Diagram showing DB structure - use a screenshot in repo
- example data ready for insertion

## DB structure

Show image with DB structure - we can see two tables, one has a foreign key that relies on the games table.

Therefore that will need to be the first we create (and also insert data when we get to that part)

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

## Intro Repo:

Show the repo, explain that it's the same one from the morning seminar.

Pseudocode out the solution:

```py
# After first table is seeded...

# Get inserted data from the first table

# Use that data to create a lookup object

# Use that lookup object to format the reviews data ready for insertion
```

**Highlight that this is just one solution and if anyone has done it a different way that is fine!**

- **If not mentioned query students if there's any extra tests we might need as we're dealing with non-primitive data > if this has been mentioned ask why.**

Insert Games:

```py
def insert_games(games):
    # loop through games
    # run an SQL insert for each game
    # Use paramterised queries to insert the values
    for game in games:
        conn.run("""
        INSERT INTO games
        (game_title, release_year, console_name, image_url)
        VALUES
        (:game_title, :release_year, :console_name, :image_url);
        """,
        game_title=game['game_title'],
        release_year=game['release_year'],
        console_name=game['console_name'],
        image_url=game['image_url']
        )

```

## Lookup Object Code

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
