from db.connection import conn


def seed(games, reviews):
    '''
        DROP ✅

        CREATE ✅

        INSERT
    '''

    # Drop tables
    conn.run('DROP TABLE IF EXISTS reviews;')
    conn.run('DROP TABLE IF EXISTS games;')

    # Create tables
    create_games_table()
    create_reviews_table()

    # Insert data
    insert_games(games)


def create_games_table():
    conn.run("""
    CREATE TABLE games (
        game_id SERIAL PRIMARY KEY,
        game_title VARCHAR(50) NOT NULL,
        release_year INT NOT NULL,
        console_name VARCHAR(50) NOT NULL,
        image_url VARCHAR NOT NULL
    );
    """)


def create_reviews_table():
    conn.run("""
    CREATE TABLE reviews (
        review_id SERIAL PRIMARY KEY,
        game_id INT REFERENCES games(game_id) NOT NULL,
        username VARCHAR(50) NOT NULL,
        comment VARCHAR NOT NULL,
        rating INT NOT NULL
    );
    """)


def insert_games(games):
    # loop through games
    # run an SQL insert for each game
    # Use pramaterised queries to insert the values
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
