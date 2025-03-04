# Optional Queries and Testing

## Learning Objectives:

- Build an endpoint that accepts optional queries with TDD
- Make use of Pydantic features to ensure query values meet the requirements
- Explore how to build up a complex SQL query from scratch.

## Intro

Introduce problem: **GET** `/api/reviews` with optional `sort_by` and `order` queries

- ask students to remind me what the url syntax is for queries

Talk through the behaviour we want - giving examples etc.

Switch to the repo for a refresher on the DB I'm using - ask students to help me write an SQL query to achieve what we want.

## FastAPI

Switch to fastAPI, show that I've already got the code for the initial GET request but no queries and that a test is written.

## First query test

Ask someone to suggest a next test:

- `sort_by` query with default order

Take suggestions for how to write the test. Work towards something that looks like this:

**Ask students for suggestions on how we could test that it's sorted correctly**:

- hardcoding data returned
- use `sorted` to sort data with Python and compare to original response data: https://docs.python.org/3/library/functions.html#sorted

```py
def test_200_returns_reviews_sorted_by_given_column_default_desc():
    """Tests that the reviews returned are sorted by the given key in
    descending order"""
    client = TestClient(app)

    response = client.get("/api/reviews?sort_by=rating")

    assert response.status_code == 200

    reviews = response.json()["reviews"]

    assert len(reviews) == 28

    sorted_reviews = sorted(
        reviews, key=lambda review: review["rating"], reverse=True
    )
    assert reviews == sorted_reviews
```

Possible solution:

- Talk about how we can deal with column - ask students if they've come across any issues when trying to parametrise column

- Talk about how it is what's known as an identifier (things such as tables, columns or other database objects) - you can find out more about what an identifier is in the postgres documentation but essentially we need to treat it slightly differently that we would do if we were parametrising a value

- pg8000 gives us a nice way of handling it: https://github.com/tlocke/pg8000?tab=readme-ov-file#many-sql-statements-cant-be-parameterized

- can insert manually with f strings or even better use the `identifier` function to escape the values and avoid SQL injection.

```py
from pg8000.native import identifier

app = FastAPI()


@app.get("/api/reviews")
def get_reviews(sort_by=None):
    try:
        conn = connect_to_db()
        query_str = """
        SELECT * FROM reviews
        """
        if sort_by:
            query_str += f"ORDER BY {identifier(sort_by)} DESC"

        reviews = conn.run(query_str)

        columns = [col["name"] for col in conn.columns]

        return format_response(columns, reviews, "reviews")
    finally:
        if conn:
            conn.close()
```

## Next query test

Ask students for next test:

- Include order query - will need a sort by as well as you can't order without it

Build a test that looks like this:

```py
def test_200_returns_reviews_sorted_by_given_column_order_specified():
    """Tests that the reviews returned are sorted by the given key in
    descending order"""
    client = TestClient(app)

    response = client.get("/api/reviews?sort_by=username&order=ASC")

    assert response.status_code == 200

    reviews = response.json()["reviews"]

    assert len(reviews) == 28

    sorted_reviews = sorted(reviews, key=lambda review: review["username"])
    assert reviews == sorted_reviews
```

Solution - add order param and f-string:

```py
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
```

**at this point see if students can see any issues with the code written - hopefully they point out the risk of SQL injection from order**

Talk about how we could handle this - leading towards Pydantic typing

## Typing

Write some tests for 422 errors:

```py
# 1:
def test_422_invalid_sort_by_query():
    """Tests that the reviews returned are sorted by the given key in
    descending order"""
    client = TestClient(app)

    response = client.get("/api/reviews?sort_by=banana")

    assert response.status_code == 422

# 2:
def test_422_invalid_order_query():
    """Tests that the reviews returned are sorted by the given key in
    descending order"""
    client = TestClient(app)

    response = client.get("/api/reviews?sort_by=rating&order=NONE")

    assert response.status_code == 422

```

Ask students if they come across any ways of typing the querys:

- FastApi's `query`:
  - https://fastapi.tiangolo.com/tutorial/query-params/
  - https://fastapi.tiangolo.com/tutorial/query-params-str-validations/

Start by using query like it is show in the docs - explore how we can use some general validation like character length etc but it still leave us open to issues like `sort_by=banana`:

```py
from fastapi import FastAPI, Query
from typing import Annotated

SortByType = Annotated[str | None, Query(max_length=9)]
OrderType = Annotated[str | None, Query(max_length=4)]


@app.get("/api/reviews")
def get_reviews(sort_by: SortByType = None, order: OrderType = "DESC"):
    ...

```

What if instead I was extra specific about what I wanted, and gave a list of exactly what could be used. Ask students if they have done anything like this, lead into a solution that looks like this:

```py
from fastapi import FastAPI, Query
from typing import Annotated, Literal

SortByType = Annotated[
    Literal["review_id", "game_id", "username", "comment", "rating"],
    Query(max_length=9),
]
OrderType = Annotated[Literal["ASC", "DESC"], Query(max_length=4)]
```

---

Round off by saying I might want to check more than just the status code, in fact I probably should as we expect some kind of error sent back to the user.

This also serves as a bit of documentation for other developers who might want to work on the code.
