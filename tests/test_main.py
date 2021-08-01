from fastapi.testclient import TestClient
import requests

from main import app

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert isinstance(response.json()["tweet"], str)


# def test_favorite_tweet():
#     response = client.post("/testTweet")
#     assert response.status_code == 200
#     assert response.json()["tweet"] is type(str)


def test_get_tweets():
    response = client.get("/tweets")
    assert response.status_code == 200
    assert isinstance(response.json()["tweets"], list)

#
# def test_delete_tweet():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json()["tweet"] is type(str)

test_index()
test_get_tweets()
