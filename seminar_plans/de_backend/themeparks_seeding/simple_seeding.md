# Temporary: Last minute Seminar change of plan

Start with Poonams previous files:

```py
# connection.py
conn = pg8000.native.Connection('danika', database="nc_games")
```

```py
# seed.py

def seed(games, reviews):
    # Drop tables
    db.run('DROP TABLE IF EXISTS reviews;')
    db.run('DROP TABLE IF EXISTS games;')


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

Now we're going to pick up from where Poonam left off with the seeding.

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

Ask students what we need to do to create a table - use `pg8000.run`

Get students to guide me through the syntax for creating a table:

```py
conn.run("""
    CREATE TABLE games (
        game_id SERIAL PRIMARY KEY,
        game_title VARCHAR NOT NULL,
        release_year INT,
        console_name VARCHAR NOT NULL,
        image_url VARCHAR
        );
    """)
```

Do the same for the reviews table - make a point to question them about setting up the foreign key:

```py
conn.run("""
    CREATE TABLE reviews (
        review_id SERIAL PRIMARY KEY,
        game_id INT NOT NULL REFERENCES games(game_id),
        username VARCHAR NOT NULL,
        comment VARCHAR NOT NULL,
        rating INT
        );
    """)
```

## Inserting data

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

# Finish Up:

Depending on time can dive into data manip a bit

# Final:

```py
# Create tables
    conn.run("""
	CREATE TABLE games (
			game_id SERIAL PRIMARY KEY,
			game_title VARCHAR NOT NULL,
			release_year INT,
			console_name VARCHAR NOT NULL,
			image_url VARCHAR
			);
	""")

    conn.run("""
	CREATE TABLE reviews (
			review_id SERIAL PRIMARY KEY,
			game_id INT NOT NULL REFERENCES games(game_id),
			username VARCHAR NOT NULL,
			comment VARCHAR NOT NULL,
			rating INT
			);
	""")

    # Insert games
    for game in games:
        insert_query = f"""
        INSERT INTO games
        (game_title, release_year, console_name, image_url)
        VALUES
        (:game_title, :release_year, :console_name, :image_url);
        """
        conn.run(insert_query, **game)

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
