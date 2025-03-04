from fastapi.testclient import TestClient
import pytest

from server import app
from db.data.index import data
from db.seed import seed


@pytest.fixture(autouse=True)
def reset_db():
    seed(**data)


def test_200_returns_reviews_no_queries():
    """Tests that the endpoint returns a list of reviews formatted correctly"""
    client = TestClient(app)

    response = client.get("/api/reviews")

    assert response.status_code == 200

    reviews = response.json()["reviews"]

    assert len(reviews) == 28

    for review in reviews:
        assert isinstance(review["review_id"], int)
        assert isinstance(review["game_id"], int)
        assert isinstance(review["username"], str)
        assert isinstance(review["comment"], str)
        assert isinstance(review["rating"], int)


def test_200_return_reviews_sorted_by_given_column_default_desc():
    test_client = TestClient(app)

    response = test_client.get("/api/reviews?sort_by=rating")

    # check status code
    assert response.status_code == 200

    reviews = response.json()["reviews"]

    assert len(reviews) == 28

    # check if reviews are sorted:
    #   - compare sorted reviews to original reviews to
    #       check if sort is correctly applied

    ratings = [review["rating"] for review in reviews]

    assert ratings == sorted(ratings, reverse=True)


def test_200_return_reviews_sorted_by_given_column_order_specified():
    test_client = TestClient(app)

    response = test_client.get("/api/reviews?sort_by=username&order=ASC")

    # check status code
    assert response.status_code == 200

    reviews = response.json()["reviews"]

    assert len(reviews) == 28

    sorted_reviews = sorted(reviews, key=lambda review: review["username"])

    assert reviews == sorted_reviews


def test_422_invalid_sort_by_query():
    """Tests that the reviews returned are sorted by the given key in
    descending order"""
    client = TestClient(app)

    response = client.get("/api/reviews?sort_by=banana")

    assert response.status_code == 422
