from fastapi import FastAPI, HTTPException
from db.connection import create_connection, close_connection
from server_utils import format_response
from pprint import pprint


app = FastAPI()


@app.get("/api/reviews/{review_id}")
def get_review_by_id(review_id: int):
    conn = create_connection()

    query_str = """
    SELECT review_id, game_title, username, comment, rating
    FROM reviews
    JOIN games ON reviews.game_id = games.game_id
    WHERE review_id = :review_id;
    """

    reviews = conn.run(query_str, review_id=review_id)
    columns = [col["name"] for col in conn.columns]

    if len(reviews) == 0:
        raise HTTPException(status_code=404, detail="Review not found")

    formatted_review = format_response(columns, reviews, "review")
    return formatted_review
