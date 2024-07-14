from fastapi import FastAPI
from typing import Literal
from pg8000.native import identifier

from db.connection import connect_to_db
from server_utils import format_response


app = FastAPI()


SortByType = Literal["review_id", "game_id", "username", "comment", "rating"]
OrderType = Literal["ASC", "DESC"]


@app.get("/api/reviews")
def get_reviews(sort_by: SortByType = None, order: OrderType = "DESC"):
    try:
        conn = connect_to_db()

        if sort_by:
            query_str = f"""
            SELECT * FROM reviews
            ORDER BY {identifier(sort_by)} {order}
            """

        else:
            query_str = """
            SELECT * FROM reviews
            """

        reviews = conn.run(query_str)
        # reviews = [ [1,4,auther_nmae,d], [a.b.c.d], ...]

        columns = [col["name"] for col in conn.columns]

        return format_response(columns, reviews, "reviews")
        # {"reviews": [
        #   {
        #       'review_id' : 1
        #               ...
        #   },
        #  .....
        # ]
        # }
    finally:
        if conn:
            conn.close()
