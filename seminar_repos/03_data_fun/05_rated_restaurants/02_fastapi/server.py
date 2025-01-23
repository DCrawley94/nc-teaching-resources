from fastapi import FastAPI
from pydantic import BaseModel
from db.connection import create_connection, close_connection

app = FastAPI()


class NewGame(BaseModel):
    game_title: str
    release_year: int
    console_name: str
    image_url: str


@app.post("/api/games", status_code=201)
def post_game(new_game: NewGame):
    # connect to db
    conn = create_connection()

    # create query string - insert
    insert_str = """
    INSERT INTO games
    (game_title, release_year, console_name, image_url)
    VALUES
    (:game_title, :release_year, :console_name, :image_url)
    RETURNING *;
    """
    # run query - using supplied game data
    inserted_game = conn.run(insert_str, **new_game.model_dump())[0]

    columns = [col["name"] for col in conn.columns]

    close_connection(conn)

    # format response - send back to client
    return format_response(columns, inserted_game)


@app.delete("/api/reviews/{review_id}", status_code=204)
def delete_review(review_id: int):
    conn = create_connection()

    delete_query = """
    DELETE FROM reviews
    WHERE review_id = :review_id;
    """

    conn.run(delete_query, review_id=review_id)

    close_connection(conn)


def format_response(columns, inserted_game):
    # formatted_game = {columns[i]: inserted_game[i] for i in range(len(columns))}
    formatted_game = dict(zip(columns, inserted_game))
    return {"game": formatted_game}
