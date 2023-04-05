
import os
import json
from typing import Union
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from pydantic import BaseModel
from fastapi import FastAPI
from dotenv import load_dotenv

from core.abstract_component import AbstractComponent

class AuthenticateGoogleSheetsAPIInputDict(BaseModel):
    credentials: Union[str, dict]

class AuthenticateGoogleSheetsAPIOutputDict(BaseModel):
    service_object: object

class AuthenticateGoogleSheetsAPI(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = json.loads(file.read())
        
        self.api_version: str = yaml_data["parameters"]["api_version"]
        self.scope: str = yaml_data["parameters"]["scope"]

    def transform(
        self, args: AuthenticateGoogleSheetsAPIInputDict
    ) -> AuthenticateGoogleSheetsAPIOutputDict:
        creds_json = args.credentials
        if isinstance(creds_json, str):
            creds = Credentials.from_service_account_info(json.loads(creds_json), scopes=[self.scope])
        else:
            creds = Credentials.from_service_account_info(creds_json, scopes=[self.scope])
        
        service = build("sheets", self.api_version, credentials=creds)
        
        return AuthenticateGoogleSheetsAPIOutputDict(service_object=service)

load_dotenv()
auth_google_sheets_api_app = FastAPI()

@auth_google_sheets_api_app.post("/transform/")
async def transform(
    args: AuthenticateGoogleSheetsAPIInputDict,
) -> AuthenticateGoogleSheetsAPIOutputDict:
    auth_google_sheets_api = AuthenticateGoogleSheetsAPI()
    return auth_google_sheets_api.transform(args)
