# FastAPI - POST/DELETE

Seminar Plan: https://docs.google.com/document/d/1SYfTXdMvHSPXFNy_iEutsrZxjjf2L4wJc_dlLTL_bIE/edit?usp=sharing

Figjam:

## Learning Objectives

- Know how to create endpoint POST endpoint with FastAPI
- Explore how a DELETE request can be handled
- Know how to define a Pydantic Model for a request body.

# Introduction

Refresher on what it means to make a POST request and what our server needs to do to handle it.

Introduce tasks:

- Post new game
- Delete review

# Post Request

Pseudocode a solution to POST - hopefully outlining the following steps:

- insert game into the database - returning inserted data
- parametrise to avoid injection
- format output to match requirements

Students lead me through a solution - **Avoid types at first**

```py
@app.post("/api/games")
def post_game(game):
    conn = create_connection()

    inserted_game = conn.run(
    """
    INSERT INTO games
    (game_title, release_year, console_name, image_url)
    VALUES
    (:game_title, :release_year, :console_name, :image_url)
    RETURNING *;
    """,
    **game)[0]

    games_columns = [col["name"] for col in conn.columns]

    close_connection(conn)

    formatted_game_data = dict(zip(games_columns, inserted_game))

    return {"game": formatted_game_data}
```

Once that's done ask if there's anything we could use to ensure that the data sent by the user has the correct structure. This should lead nicely into a discussion about Pydantic types.

Get someone to talk me through the creation of a Pydantic Model.

Steps for making a model:

- Define new class which inherits from Pydantics base model
- Define fields on this model and set the expected data types
- Use type annotation to make sure that the game is the correct type

```py
from pydantic import BaseModel


class Game(BaseModel):
    game_title: str
    release_year: int
    console_name: str
    image_url: str

@app.post("/api/games")
def post_game(game: Game):
    # ...

    # conn.run args:
    **dict(game)
```

**Demo what happens if we fuck up the request**

---

Point out that the requirements asked for a 201 status but we get a 200. How can we fix this?

# Delete Request

Ask for students to talk through the process of making the DELETE endpoint.

- How can we get the ID from the URL? No more regex 🎉
- Paramterise the ID
- Set the status code

Anything else? Do we need to return anything?

```py
@app.delete("/api/reviews/{review_id}", status_code=204)
def delete_review(review_id: int):
    conn = create_connection()

    conn.run(
        "DELETE FROM reviews WHERE review_id = :review_id;",
        review_id=review_id,
    )

    close_connection(conn)
```
