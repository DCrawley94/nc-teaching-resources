from fastapi import FastAPI, Query
from typing import Annotated, Literal

from db.connection import connect_to_db
from server_utils import format_response

from pg8000.native import identifier


app = FastAPI()

SortByType = Annotated[str | None, Query(max_length=9)]


@app.get("/api/reviews")
def get_reviews(sort_by=None, order="DESC"):
    try:
        conn = connect_to_db()
        query_str = """
        SELECT * FROM reviews
        """
        if sort_by:
            query_str += f"ORDER BY {identifier(sort_by)} {order}"

        reviews = conn.run(query_str)

        columns = [col["name"] for col in conn.columns]

        return format_response(columns, reviews, "reviews")
    finally:
        if conn:
            conn.close()
