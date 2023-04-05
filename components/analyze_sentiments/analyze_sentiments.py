
import os

from typing import Any, Dict, List, Union
import yaml
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob

from core.abstract_component import AbstractComponent


class AnalyzeSentimentsInputDict(BaseModel):
    tweets_list: List[Dict[str, Any]]


class AnalyzeSentimentsOutputDict(BaseModel):
    sentiments_list: List[Dict[str, Union[str, float]]]


class AnalyzeSentiments(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()

    def transform(
        self, args: AnalyzeSentimentsInputDict
    ) -> AnalyzeSentimentsOutputDict:
        print(f"Executing the transform of the {type(self).__name__} component...")

        sentiments_list = []

        for tweet in args.tweets_list:
            handle = tweet["handle"]
            tweet_content = tweet["tweet"]
            sentiment_score = TextBlob(tweet_content).sentiment.polarity
            updated_dict = {
                "handle": handle,
                "tweet": tweet_content,
                "sentiment": sentiment_score,
            }
            sentiments_list.append(updated_dict)

        return AnalyzeSentimentsOutputDict(sentiments_list=sentiments_list)


load_dotenv()
analyze_sentiments_app = FastAPI()


@analyze_sentiments_app.post("/transform/")
async def transform(
    args: AnalyzeSentimentsInputDict,
) -> AnalyzeSentimentsOutputDict:
    analyze_sentiments = AnalyzeSentiments()
    return analyze_sentiments.transform(args)
