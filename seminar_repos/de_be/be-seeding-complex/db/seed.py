from db.connection import conn
from db.utils import create_games_lookup, format_reviews
from pprint import pprint


def seed(games, reviews):
    # Drop tables
    conn.run("DROP TABLE IF EXISTS reviews;")
    conn.run("DROP TABLE IF EXISTS games;")

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

