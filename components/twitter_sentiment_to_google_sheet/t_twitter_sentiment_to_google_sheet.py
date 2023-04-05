
# Import necessary libraries and the component
import pytest
from pydantic import ValidationError
from typing import List, Dict, Any
from fastapi.testclient import TestClient
from twitter_sentiment_to_google_sheet import (
    TwitterHandlesIn,
    GoogleSheetURLOut,
    FastAPI,
    transform,
)

# Define test cases with mocked input and expected output data
mocked_twitter_handles_in_valid = [
    {
        "handles": ["test_handle1", "test_handle2"],
        "credentials": {"api_key": "my_test_key", "api_secret_key": "my_test_secret_key"},
    },
    {
        "handles": [],
        "credentials": {"api_key": "my_test_key", "api_secret_key": "my_test_secret_key"},
    },
]

mocked_twitter_handles_in_invalid = [
    {"handles": "test_handle1", "credentials": {"api_key": "my_test_key"}},
    {
        "handles": ["test_handle1", "test_handle2"],
        "credentials": "invalid_credentials",
    },
]

mocked_google_sheet_url_out = [
    {"url": "https://docs.google.com/spreadsheets/test_url1"}, {"url": ""},
]

# Use @pytest.mark.parametrize to create multiple test scenarios
@pytest.mark.parametrize(
    "input_data, expected_output_data",
    [
        (mocked_twitter_handles_in_valid[0], mocked_google_sheet_url_out[0]),
        (mocked_twitter_handles_in_valid[1], mocked_google_sheet_url_out[1]),
    ],
)
def test_transform(input_data: Dict, expected_output_data: Dict) -> None:
    # Call the component's transform() method and assert output matches expected output.
    input_model = TwitterHandlesIn(**input_data)
    output_model = transform(input_model)
    assert output_model.url == expected_output_data["url"]

    # Alternative approach without the transform function:
    # client = TestClient(FastAPI)
    # response = client.post("/transform/", json=input_data)
    # assert response.status_code == 200
    # assert response.json()["url"] == expected_output_data["url"]

# Include error handling and edge case scenarios, if applicable.
@pytest.mark.parametrize("input_data", mocked_twitter_handles_in_invalid)
def test_invalid_input_data(input_data: Dict) -> None:
    # Test that a ValidationError is raised when input data is invalid.
    with pytest.raises(ValidationError):
        TwitterHandlesIn(**input_data)
