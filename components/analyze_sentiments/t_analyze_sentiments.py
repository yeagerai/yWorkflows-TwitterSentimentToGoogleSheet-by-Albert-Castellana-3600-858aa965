
import pytest
from pydantic import ValidationError
from your_module import AnalyzeSentiments, AnalyzeSentimentsInputDict, AnalyzeSentimentsOutputDict

# Create test cases with mocked input and expected output data
test_cases = [
    (
        AnalyzeSentimentsInputDict(
            tweets_list=[
                {"handle": "user1", "tweet": "I love this product!"},
                {"handle": "user2", "tweet": "This is the worst!"},
            ]
        ),
        AnalyzeSentimentsOutputDict(
            sentiments_list=[
                {"handle": "user1", "tweet": "I love this product!", "sentiment": 0.5},
                {"handle": "user2", "tweet": "This is the worst!", "sentiment": -1.0},
            ]
        ),
    ),
    (
        AnalyzeSentimentsInputDict(tweets_list=[]),
        AnalyzeSentimentsOutputDict(sentiments_list=[]),
    ),
]

# Use @pytest.mark.parametrize to create multiple test scenarios
@pytest.mark.parametrize("input_data, expected_output", test_cases)
def test_analyze_sentiments(input_data, expected_output):
    component = AnalyzeSentiments()
    output = component.transform(input_data)

    assert output == expected_output


def test_analyze_sentiments_input_validation():
    with pytest.raises(ValidationError):
        AnalyzeSentimentsInputDict(tweets_list=[{"missing_handle": "user1", "tweet": "I love this product!"}])

