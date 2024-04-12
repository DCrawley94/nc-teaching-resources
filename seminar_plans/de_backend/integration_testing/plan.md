# Plan

## Learning Objectives

-

## Intro

Reminder of DB - same as previous two seminars so should be familiar with it.

## Part 1: GET

Introduce the plan for the session
Endpoint: `/api/reviews/:review_id`
Response:

```json
{
	"review": {
		"review_id": 1,
		"game_title": "Skyrim 2",
		"username": "danika",
		"comment": "Very good",
		"rating": 5
	}
}
```

Pick on someone to identify the first test:

- status 200, returns correct review

Ask for suggestions of other tests:

- status 404, no review found
- status 422, malformed review_id

Ask for a volunteer to talk me through writing this test:

Tests:

- status 200, returns correct review

**Switch to VSCode**

### 200 - review returned

Have someone walk me through how I can write a test for the 200 response - explain that I have the test data ready to go I just need help with the structure of the test.

What is the order that we need to do things in?

Possible test:

```py
class TestGetReviewByID:
    def test_200_review_returned(self):
        client = TestClient(app)
        expected_json = {
            'review': {
            'comment': (
                "Skate ipsum dolor sit amet, alley oop vert mute-air Colby "
                "Carter flail 180 berm. Half-cab camel back ollie transition "
                "ledge Wes Humpston 1080. Carve casper switch kickturn late "
                "downhill. Hardware nosebone Rick McCrank bluntslide bigspin "
                "steps egg plant. Slap maxwell roll-in airwalk fast plant "
                "fastplant pivot."
            ),
            'game_title': 'Donkey Kong',
            'rating': 4,
            'review_id': 2,
            'username': 'rogersop',
            }
        }
        response = client.get('/api/reviews/2')
        assert response.status_code == 200
        assert response.json() == expected_json
```

Once that's done ask someone else to talk me through a solution.

Questions to ask during:

- Can anyone tell me how to implement a parametric endpoint with FastAPI?
- How can we get access to the `game_title`?
- How can we handle the case where the function errors before we manage to close the db connection?

Possible solution:

```py
from db.connection import connect_to_db
from server_utils import format_response

# ...

@app.get('/api/reviews/{review_id}')
def get_review_by_id(review_id): # this can be typed - will need to be untyped to see later test fail
    conn = None
    try:
        conn = connect_to_db()
        review = conn.run("""
        SELECT review_id, game_title, username, comment, rating
        FROM reviews
        JOIN games on games.game_id = reviews.game_id
        WHERE review_id = :review_id;
        """, review_id = review_id)

        columns = [col['name'] for col in conn.columns]
        response = format_response(columns, review, "review")
        return response
    finally:
        if conn:
            conn.close()
```

### 404 - no review

Again get help writing the test. Questions:

- How do we send back a custom error response? - `HTTPException`
- what format will the response body be in if we manually raise a HTTP exception? : {"detail": "dsnkjnfjn"}

Possible test:

```py
def test_404_no_review(self):
    client = TestClient(app)
    expected_json = {'detail': 'No review with id 99999'}
    response = client.get('/api/reviews/99999')
    assert response.status_code == 404
    assert response.json() == expected_json
```

Possible handling in the endpoint:

```py
from fastapi  import FastAPI, HTTPException
#  ....
if len(review) == 0:
    raise HTTPException(
        status_code=404, detail=f"No review with id {review_id}")
```

### 400/422 - malformed review

More help with test.

Things to ask:

- What status code would you expect from this?
- will this pass straight away?
- pros/cons of pydantic approach - [400](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#client_error_responses) might be a more appropriate status code but it is not an exact science. It's very useful being able to get pydantic to do the work for us and there are ways to override the status code if we want to.

Regardless we do want to test it:

```py
def test_422_malformed_review_id(self):
    client = TestClient(app)
    response = client.get('/api/reviews/not_an_id')
    assert response.status_code == 422
```

Possible Solution:

```py
@app.get('/api/reviews/{review_id}')
def get_review_by_id(review_id:int):  # This is the key part!
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
```

## Part 2: POST

Talk about POST on Figjam

Post game:

```json
{
	"game_title": "Skyrim 2",
	"release_year": 2024,
	"console_name": "Playstation 2",
	"image_url": "https://www.nexusmods.com/skyrimspecialedition/mods/104031"
}
```

What might we want to test about the POST request?

- 201 - return game
- 400/422 - malformed request body

What might we want to do if we're repeatedly running these tests?

- seeding fixture

```py
# seeding fixture:
from db.data.index import data
from db.seed import seed
import pytest

@pytest.fixture(autouse=True)
def reset_db():
    seed(**data)
```

### 201 - return game

possible test:

```py
class TestPostGame:
    def test_201_game_returned(self):
        client = TestClient(app)
        new_game = {
            "game_title": "Skyrim 2",
            "release_year": 2024,
            "console_name": "Playstation 2",
            "image_url": "test_url"
        }
        expected_response_body = {
            'game': {
                'game_id': 4,
                'game_title': 'Skyrim 2',
                'release_year': 2024,
                'console_name': 'Playstation 2',
                'image_url': 'test_url'
            }
        }
        response = client.post('/api/games', json=new_game)
        assert response.status_code == 201
        assert response.json() == expected_response_body
```

possible solution:

```py
@app.post('/api/games', status_code=201)
def post_game(new_game):
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
```

### 400/422 - malformed game

possible test:

```py
def test_422_malformed_game(self):
    client = TestClient(app)
    new_game = {
        "game_title": "Skyrim 2",
        "console_name": "Playstation 2",
        "image_url": "test_url"
    }
    response = client.post('/api/games', json=new_game)
    assert response.status_code == 422
```

pydantic type:

```py
from pydantic import BaseModel


class NewGame(BaseModel):
    game_title: str
    release_year: int
    console_name: str
    image_url: str
```

possible solution:

```py
@app.post('/api/games', status_code=201)
def post_game(new_game: NewGame):  # Important part!
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
```
