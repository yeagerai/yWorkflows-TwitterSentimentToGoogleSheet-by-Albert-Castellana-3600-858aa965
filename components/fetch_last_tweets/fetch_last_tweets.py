
import os
from typing import List

import yaml
import tweepy
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel, Field

from core.abstract_component import AbstractComponent


class TwitterCredentials(BaseModel):
    api_key: str
    api_secret_key: str
    access_token: str
    access_token_secret: str


class FetchLastTweetsInputDict(BaseModel):
    twitter_handles: List[str]
    twitter_credentials: TwitterCredentials


class FetchLastTweetsOutputDict(BaseModel):
    last_tweets: List[dict] = Field(
        [],
        description="A list of dictionaries containing the Twitter handle and its corresponding last tweet."
    )


class FetchLastTweets(AbstractComponent):
    def transform(
        self, args: FetchLastTweetsInputDict
    ) -> FetchLastTweetsOutputDict:
        auth = tweepy.OAuthHandler(
            args.twitter_credentials.api_key, args.twitter_credentials.api_secret_key
        )
        auth.set_access_token(
            args.twitter_credentials.access_token,
            args.twitter_credentials.access_token_secret,
        )

        api = tweepy.API(auth)

        last_tweets = []
        for handle in args.twitter_handles:
            tweets = api.user_timeline(screen_name=handle, count=1)
            if tweets:
                tweet = tweets[0].text
                last_tweets.append({"handle": handle, "tweet": tweet})

        return FetchLastTweetsOutputDict(last_tweets=last_tweets)


load_dotenv()
fetch_last_tweets_app = FastAPI()


@fetch_last_tweets_app.post("/transform/")
async def transform(
    args: FetchLastTweetsInputDict,
) -> FetchLastTweetsOutputDict:
    fetch_last_tweets = FetchLastTweets()
    return fetch_last_tweets.transform(args)
