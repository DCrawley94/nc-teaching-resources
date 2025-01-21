from fastapi import FastAPI
from pydantic import BaseModel
from db.connection import create_connection, close_connection

app = FastAPI()


class Game(BaseModel):
    game_title: str
    release_year: int
    console_name: str
    image_url: str


@app.get("/api/games/{game_id}")
def get_game_by_id(game_id: int):
    conn = create_connection()
    query = """
    SELECT * FROM games
    WHERE game_id = :game_id;
    """

    game_data = conn.run(query, game_id=game_id)[0]
    columns = [col["name"] for col in conn.columns]

    close_connection(conn)

    formatted_game_data = dict(zip(columns, game_data))

    return {"game": formatted_game_data}


@app.post("/api/games", status_code=201)
def post_game(game: Game):
    conn = create_connection()
    query = """
    INSERT INTO games
    (game_title, release_year, console_name, image_url)
    VALUES
    (:game_title, :release_year, :console_name, :image_url)
    RETURNING *;
    """

    inserted_game = conn.run(query, **dict(game))[0]
    columns = [col["name"] for col in conn.columns]

    close_connection(conn)

    formatted_game_data = dict(zip(columns, inserted_game))

    return {"game": formatted_game_data}
