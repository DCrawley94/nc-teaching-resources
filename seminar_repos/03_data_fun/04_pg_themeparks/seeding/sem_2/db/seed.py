from pprint import pprint


def seed(conn, games, reviews):
    print("seeding data ...")
    # Drop tables

    conn.run("DROP TABLE IF EXISTS reviews;")
    conn.run("DROP TABLE IF EXISTS games;")

    # Create tables
    create_games_table(conn)
    create_reviews_table(conn)

    # Insert games
    insert_games(conn, games)

    # access to the inserted game data (game_id)
    games_data = conn.run("SELECT game_title, game_id FROM games;")

    # - some way to link game_title (review data)
    # to the game_id in inserted games
    game_id_lookup = {game[0]: game[1] for game in games_data}

    # - when inserting reviews - we can replace title with appropriate id
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


def create_games_lookup(inserted_games):
    """
    Should accept nested list of games and return dictionary
        containing game title and game id
    """
    return {game[1]: game[0] for game in inserted_games}


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


def create_insert_reviews_query(rows):
    start_str = """
    INSERT INTO reviews
    (game_id, username, comment, rating)
    VALUES
    """

    rows_to_insert = ",\n".join(
        [
            f"({game_id}, {username}, {comment}, {rating})"
            for game_id, username, comment, rating in rows
        ]
    )

    pprint(rows_to_insert)
