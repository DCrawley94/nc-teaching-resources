from fastapi.testclient import TestClient
from server import app


class TestGetReviewByID:
    def test_200_review_returned(self):
        expected_body = {
            "review": {
                "comment": (
                    "Skate ipsum dolor sit amet, alley oop vert mute-air Colby "
                    "Carter flail 180 berm. Half-cab camel back ollie transition "
                    "ledge Wes Humpston 1080. Carve casper switch kickturn late "
                    "downhill. Hardware nosebone Rick McCrank bluntslide bigspin "
                    "steps egg plant. Slap maxwell roll-in airwalk fast plant "
                    "fastplant pivot."
                ),
                "game_title": "Donkey Kong",
                "rating": 4,
                "review_id": 2,
                "username": "rogersop",
            }
        }

        client = TestClient(app)

        response = client.get("/api/reviews/2")

        assert response.status_code == 200
        assert response.json() == expected_body

    def xtest_404_no_review_found(self):
        client = TestClient(app)

        response = client.get("/api/reviews/999999")
        expected_body = {"detail": "Review not found"}

        assert response.status_code == 404
        assert response.json() == expected_body

    def xtest_422_invalid_id(self):
        client = TestClient(app)

        response = client.get("/api/reviews/not-an-id")

        assert response.status_code == 422
