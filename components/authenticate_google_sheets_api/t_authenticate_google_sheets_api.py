
# tests/test_authenticate_google_sheets_api.py

import pytest
import json
from google.oauth2.service_account import Credentials
from pydantic import ValidationError
from core.authenticate_google_sheets_api import (
    AuthenticateGoogleSheetsAPI,
    AuthenticateGoogleSheetsAPIInputDict,
    AuthenticateGoogleSheetsAPIOutputDict,
)

# Mocked credentials as str or dict
MOCKED_CREDENTIALS_STR = json.dumps({
    "type": "service_account",
    "project_id": "fake-project-id",
    "private_key_id": "fake-private-key-id",
    "private_key": "fake-private-key",
    "client_email": "fake-client-email",
    "client_id": "fake-client-id",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/test%40example.iam.gserviceaccount.com"
})
MOCKED_CREDENTIALS_DICT = json.loads(MOCKED_CREDENTIALS_STR)

# Test cases with mocked input and expected output data
test_cases = [
    {
        "input_data": {"credentials": MOCKED_CREDENTIALS_STR},
        "expected_output": {"service_object": Credentials},
    },
    {
        "input_data": {"credentials": MOCKED_CREDENTIALS_DICT},
        "expected_output": {"service_object": Credentials},
    },
]


@pytest.mark.parametrize("test_case", test_cases)
def test_authenticate_google_sheets_api(test_case):
    # Instantiate the component
    auth_google_sheets_api = AuthenticateGoogleSheetsAPI()

    # Prepare input data
    input_data = AuthenticateGoogleSheetsAPIInputDict(**test_case["input_data"])

    # Call the transform() method
    output_data = auth_google_sheets_api.transform(input_data)

    # Assert the output matches the expected output
    assert isinstance(output_data.service_object, test_case["expected_output"]["service_object"])

    # Assert the output is an instance of AuthenticateGoogleSheetsAPIOutputDict
    assert isinstance(output_data, AuthenticateGoogleSheetsAPIOutputDict)


def test_invalid_input_data():
    # Test for invalid input data (credentials is None)
    with pytest.raises(ValidationError) as exc_info:
        input_data = AuthenticateGoogleSheetsAPIInputDict(credentials=None)
    assert "field required" in str(exc_info.value)
