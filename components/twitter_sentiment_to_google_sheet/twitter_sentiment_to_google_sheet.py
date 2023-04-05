
import typing
from typing import List, Dict, Any
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from core.workflows.abstract_workflow import AbstractWorkflow

class TwitterHandlesIn(BaseModel):
    handles: List[str]
    credentials: Dict[str, Any]

class GoogleSheetURLOut(BaseModel):
    url: str

class TwitterSentimentToGoogleSheet(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: TwitterHandlesIn, callbacks: typing.Any
    ) -> GoogleSheetURLOut:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        google_sheet_url = results_dict[-1].url
        out = GoogleSheetURLOut(url=google_sheet_url)
        return out

load_dotenv()
twitter_sentiment_to_google_sheet_app = FastAPI()

@twitter_sentiment_to_google_sheet_app.post("/transform/")
async def transform(
    args: TwitterHandlesIn,
) -> GoogleSheetURLOut:
    twitter_sentiment_to_google_sheet = TwitterSentimentToGoogleSheet()
    return await twitter_sentiment_to_google_sheet.transform(args, callbacks=None)
