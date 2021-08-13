import os
import sys
from datetime import datetime

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)

from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.core.main import app

client = TestClient(app)

class TestRoutes:
    def test_index(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"msg": "Hello World"}

    def test_generate_tweet(self):
        response = client.get("/tweets")
        assert response.status_code == 200
        assert type(response.json()["tweet"]) is str

    def test_create_tweet(self):
        response = client.post("/tweets/test300")
        assert response.status_code == 200
        assert response.json()['data'][0]["tweet"] == "test300"
        assert response.json()["message"] == "Tweet added successfully."

    def test_get_all_tweets(self):
        response = client.get("/tweets/all")
        assert response.status_code == 200
        assert type(response.json()["tweets"]) is list

    def test_delete_tweet(self):
        # Add Tweet and Get tweet id to test delete
        response = client.post("/tweets/test300")
        assert response.status_code == 200
        assert response.json()['data'][0]["tweet"] == "test300"
        assert response.json()["message"] == "Tweet added successfully."
        id = response.json()['data'][0]["_id"]

        # Test Delete Tweet that was just added to db
        response = client.delete("/tweets/" + id)
        assert response.status_code == 200
        assert response.json()["data"] == ['Tweet with ID: ' + id + ' removed']
        assert response.json()["message"] == 'Tweet deleted successfully'

        # Test Delete Tweet that was just deleted from db
        response = client.delete("/tweets/" + id)
        assert response.status_code == 200
        assert response.json()["error"] == 'An error occurred'
        assert response.json()["code"] == 404
        assert response.json()["message"] == "Tweet with id " + id + " doesn't exist"
