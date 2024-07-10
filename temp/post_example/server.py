from fastapi import FastAPI
from db.connection import connect_to_db
from server_utils import format_response
from pydantic import BaseModel


app = FastAPI()


# Pydantic type for incoming data
class NewGame(BaseModel):
    game_title: str
    release_year: int
    console_name: str
    image_url: str


@app.post("/api/games", status_code=201)
def post_game(new_game: NewGame):
    conn = connect_to_db()

    inserted_game = conn.run(
        """
        INSERT INTO games
        (game_title, release_year, console_name, image_url)
        VALUES
        (:game_title, :release_year, :console_name, :image_url)
        RETURNING *;
        """,
        game_title=new_game.game_title,
        release_year=new_game.release_year,
        console_name=new_game.console_name,
        image_url=new_game.image_url,
    )
    columns = [col["name"] for col in conn.columns]

    formatted_response = format_response(columns, inserted_game, "game")

    return formatted_response
