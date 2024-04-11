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
- How can we handle the case where the function errors before we manage to close the db connection?

Possible solution:

```py
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

### 422 - malformed review

## Part 2: POST

Talk about POST:

Post game:

```json
{
	"game_title": "Skyrim 2",
	"release_year": 2024,
	"console_name": "Playstation 2",
	"image_url": "https://www.nexusmods.com/skyrimspecialedition/mods/104031"
}
```
