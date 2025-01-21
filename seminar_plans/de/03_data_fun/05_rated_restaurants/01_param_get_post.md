# FastAPI - PARAMETRIC GET + POST

Figjam: https://www.figma.com/board/tfh7Fb1XkO45ITBymsImg6/FastAPI-1?node-id=0-1&t=yUhfOznrVz855hYc-1

## Learning Objectives

- Know how to create endpoint POST endpoint with FastAPI
- Explore how a DELETE request can be handled
- Know how to define a Pydantic Model for a request body.

# Introduction

Refresher on what it means to make a POST request and what our server needs to do to handle it.

Introduce tasks:

- Get game by id
- Post game

# Get Game by ID

Start with pseudocode, like this:

- access ID from url
- use ID to query DB
- format data to meet spec
- return formatted game

Students lead me through a solution

**TO RUN SERVER:**

```sh
fastapi dev server.py
```

---

## Solution

```py
from fastapi import FastAPI
# from pydantic import BaseModel - NOT NEEDED YET
from db.connection import create_connection, close_connection

app = FastAPI()

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
```

# Post Request

Pseudocode a solution to POST - hopefully outlining the following steps:

- define new type for user submitted game
- insert game into the database - returning inserted data
- parametrise to avoid injection
- format output to match requirements

This should lead nicely into a discussion about Pydantic types.

Get someone to talk me through the creation of a Pydantic Model.

Steps for making a model:

- Define new class which inherits from Pydantics base model
- Define fields on this model and set the expected data types
- Use type annotation to make sure that the game is the correct type

Students lead me through a solution

**TO RUN SERVER:**

```sh
fastapi dev server.py
```

---

**If no type specified might have an error like this:**

```json
{
	"detail": [
		{
			"type": "missing",
			"loc": ["query", "game"],
			"msg": "Field required",
			"input": null
		}
	]
}
```

Can fix with:

```py
# Type annotation
def post_game(game: Game):
    ...
```

---

```py
...
from pydantic import BaseModel
...


class Game(BaseModel):
    game_title: str
    release_year: int
    console_name: str
    image_url: str


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

```

**Demo what happens if we fuck up the request**

---

Point out that the requirements asked for a 201 status but we get a 200. How can we fix this?

# Possible Extension

Show what happens when you get a game by an id that doesn't exists in the DB

Is this what we want?

How else might we want it to behave?
