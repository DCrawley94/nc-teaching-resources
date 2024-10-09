from fastapi import FastAPI
from pydantic import BaseModel
from db.connection import create_connection, close_connection

app = FastAPI()


# BaseModel
class NewGame(BaseModel):
    game_title: str
    release_year: int
    console_name: str
    image_url: str


# Post game


# create function with post decorator
@app.post("/api/games", status_code=201)
def post_game(new_game: NewGame):
    # create DB connection
    conn = create_connection()

    insert_query = """
    INSERT INTO games
    (game_title, release_year, console_name, image_url)
    VALUES
    (:game_title, :release_year, :console_name, :image_url)
    RETURNING *;
    """
    # run INSERT query - parameterisation?
    rows = conn.run(insert_query, **dict(new_game))[0]
    columns = [col["name"] for col in conn.columns]

    close_connection(conn)

    # do any necessary data formatting before seding back to the user
    new_game = dict(zip(columns, rows))

    return {"game": new_game}


# Delete game
@app.delete("/api/reviews/{review_id}")
def delete_review(review_id):
    conn = create_connection()

    delete_query = """
    DELETE FROM reviews WHERE review_id = :review_id;
    """

    conn.run(delete_query, review_id=review_id)

    return {"msg": "hello"}
