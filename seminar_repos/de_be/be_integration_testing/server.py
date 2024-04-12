from fastapi import FastAPI, HTTPException
from db.connection import connect_to_db
from server_utils import format_response
from pg8000.exceptions import DatabaseError


app = FastAPI()


@app.get('/api/reviews/{review_id}')
def get_review_by_id(review_id):
    conn = None
    try:
        conn = connect_to_db()
        query = """
        SELECT review_id, game_title, username, comment, rating 
        FROM reviews
        INNER JOIN games ON games.game_id = reviews.game_id
        WHERE review_id = :review_id;
        """

        review = conn.run(query, review_id=review_id)

        if not len(review):
            raise HTTPException(
                status_code=404, detail=f"No review found with id {review_id}"
            )

        columns = [col['name'] for col in conn.columns]
        response = format_response(columns, review, "review")

        return response
    except DatabaseError as db_error:
        error = db_error.args[0]
        error_code = error['C']
        error_message = error['M']
        if error_code == '22P02':
            raise HTTPException(
                status_code=400, 
                detail=f"review_id should be an integer - {error_message}"
            )
    finally:
        if conn:
            conn.close()
