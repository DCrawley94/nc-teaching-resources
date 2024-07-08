from connection import conn

def seed(games, reviews):
    print('seeding data ...')
    # Drop tables
    conn.run('DROP TABLE IF EXISTS reviews;')
    conn.run('DROP TABLE IF EXISTS games;')

    # Create tables
    create_games_table()
    create_reviews_table()



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
    """Should insert games data into the games table"""
    pass
