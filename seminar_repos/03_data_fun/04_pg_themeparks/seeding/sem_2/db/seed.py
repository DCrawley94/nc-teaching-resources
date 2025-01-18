from pprint import pprint


def seed(conn, games, reviews):
    print("seeding data ...")
    # Drop tables

    print("dropping tables ...")
    conn.run("DROP TABLE IF EXISTS reviews;")
    conn.run("DROP TABLE IF EXISTS games;")

    # Create tables
    print("creating tables ...")
    create_games_table(conn)
    create_reviews_table(conn)

    # Insert games
    print("inserting games ...")
    insert_games(conn, games)

    # Create a dictionary which links game_title > game_id
    # Lookup Dictionary

    # Select data from games table
    game_data = conn.run("SELECT game_id, game_title FROM games;")

    # Pass data to lookup util
    game_id_lookup = create_game_lookup(game_data)

    print("inserting reviews ...")
    insert_reviews(conn, reviews, game_id_lookup)


def create_games_table(conn):
    conn.run("""
    CREATE TABLE games (
        game_id SERIAL PRIMARY KEY,
        game_title VARCHAR(50) NOT NULL,
        release_year INT NOT NULL,
        console_name VARCHAR(50) NOT NULL,
        image_url VARCHAR NOT NULL
    );
    """)


def create_reviews_table(conn):
    conn.run(
        """
        CREATE TABLE reviews (
            review_id SERIAL PRIMARY KEY,
            game_id INT REFERENCES games(game_id),
            username VARCHAR(50) NOT NULL,
            comment VARCHAR NOT NULL,
            rating INT
        );
        """
    )


def insert_games(conn, games):
    """Should insert games data into the games table"""

    insert_str = """
    INSERT INTO games
    (game_title, release_year, console_name, image_url)
    VALUES
    (:game_title, :release_year, :console_name, :image_url);
    """

    for game in games:
        game_title = game["game_title"]
        release_year = game["release_year"]
        console_name = game["console_name"]
        image_url = game["image_url"]

        conn.run(
            insert_str,
            game_title=game_title,
            release_year=release_year,
            console_name=console_name,
            image_url=image_url,
        )


def create_game_lookup(game_rows):
    return {game_name: game_id for game_id, game_name in game_rows}


def insert_reviews(conn, reviews, game_id_lookup):
    insert_str = """
    INSERT INTO reviews
    (game_id, username, comment, rating)
    VALUES
    (:game_id, :username, :comment, :rating);
    """

    for review in reviews:
        username = review["username"]
        game_id = game_id_lookup[review["game_title"]]
        comment = review["comment"]
        rating = review["rating"]

        conn.run(
            insert_str,
            username=username,
            game_id=game_id,
            comment=comment,
            rating=rating,
        )
