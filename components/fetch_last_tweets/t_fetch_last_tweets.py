
import pytest
import tweepy
from core.abstract_component import AbstractComponent
from pydantic import BaseModel
from fastapi.testclient import TestClient

from component import FetchLastTweets, FetchLastTweetsInputDict, FetchLastTweetsOutputDict, fetch_last_tweets_app

# We'll use FastAPI's TestClient to test our endpoint
client = TestClient(fetch_last_tweets_app)

# Create a test TwitterCredentials instance for testing
test_credentials = {"api_key": "test_api_key",
                    "api_secret_key": "test_api_secret_key",
                    "access_token": "test_access_token",
                    "access_token_secret": "test_access_token_secret"}

# Define test cases with mocked input and expected output data
test_data = [
    # Case 1: basic input with two twitter handles
    {
        "input": FetchLastTweetsInputDict(
            twitter_handles=["handle1", "handle2"],
            twitter_credentials=test_credentials
        ),
        "output": [
            {"handle": "handle1", "tweet": "Test tweet 1"},
            {"handle": "handle2", "tweet": "Test tweet 2"}
        ]
    },
    # Case 2: handle with no tweets
    {
        "input": FetchLastTweetsInputDict(
            twitter_handles=["handle_no_tweets"],
            twitter_credentials=test_credentials
        ),
        "output": []
    }
]


# Use tweepy API mock to return last tweets as defined in test_data
class TweepyAPIMock:
    @staticmethod
    def user_timeline(screen_name, count=1):
        for case in test_data:
            for handle_tweet in case['output']:
                if screen_name == handle_tweet['handle']:
                    return [type('Tweet', (object,), {'text': handle_tweet["tweet"]})]

        return []


def mock_tweepy_api(*args, **kwargs):
    return TweepyAPIMock()


@pytest.fixture(autouse=True)
def mock_tweepy(monkeypatch):
    monkeypatch.setattr(tweepy.API, "__init__", mock_tweepy_api)
    return tweepy.API()


# Use @pytest.mark.parametrize to create multiple test scenarios
@pytest.mark.parametrize("test_input,expected_output", [(case["input"], case["output"]) for case in test_data])
def test_fetch_last_tweets(test_input: FetchLastTweetsInputDict, expected_output: list):
    # Call the component's transform() method
    response = client.post("/transform/", json=test_input.dict())

    # Assert response status code and output data
    assert response.status_code == 200
    fetched_tweets = response.json()["last_tweets"]
    assert len(fetched_tweets) == len(expected_output)

    for idx, fetched_data in enumerate(fetched_tweets):
        assert fetched_data["handle"] == expected_output[idx]["handle"]
        assert fetched_data["tweet"] == expected_output[idx]["tweet"]
