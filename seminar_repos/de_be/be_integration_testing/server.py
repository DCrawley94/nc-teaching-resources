from db.connection import connect_to_db
from server_utils import format_response
from fastapi  import FastAPI, HTTPException
from pydantic import BaseModel


class NewGame(BaseModel):
    game_title: str
    release_year: int
    console_name: str
    image_url: str

app = FastAPI()

@app.get('/api/reviews/{review_id}')
def get_review_by_id(review_id: int):
    conn = None
    try:
        conn = connect_to_db()
        review = conn.run("""
        SELECT review_id, game_title, username, comment, rating 
        FROM reviews
        JOIN games on games.game_id = reviews.game_id
        WHERE review_id = :review_id;
        """, review_id = review_id)

        if len(review) == 0:
            raise HTTPException(
                status_code=404, detail=f"No review with id {review_id}")

        columns = [col['name'] for col in conn.columns]
        response = format_response(columns, review, "review")
        return response
    finally:
        if conn:
            conn.close()


@app.post('/api/games', status_code=201)
def post_game(new_game: NewGame):
    conn = None
    try:
        conn = connect_to_db()
        new_game = conn.run("""
        INSERT INTO games
        (game_title, release_year, console_name, image_url)
        VALUES
        (:game_title, :release_year, :console_name, :image_url)
        RETURNING *;
        """, **dict(new_game))
        columns = [col['name'] for col in conn.columns]
        response = format_response(columns, new_game, "game")
        return response
    finally:
        if conn:
            conn.close()
