from pprint import pprint


def seed(conn, games, reviews):
    print("seeding data ...")
    # Drop tables
    conn.run("DROP TABLE IF EXISTS reviews;")
    conn.run("DROP TABLE IF EXISTS games;")

    # Create tables
    create_games_table(conn)
    create_reviews_table(conn)

    inserted_games = insert_games(conn, games)
    formatted_reviews = format_reviews(inserted_games, reviews)

    insert_reviews(conn, formatted_reviews)


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
    conn.run("""
    CREATE TABLE reviews (
        review_id SERIAL PRIMARY KEY,
        game_id INT REFERENCES games(game_id) NOT NULL,
        username VARCHAR(50) NOT NULL,
        comment VARCHAR NOT NULL,
        rating INT NOT NULL
    );
    """)


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
