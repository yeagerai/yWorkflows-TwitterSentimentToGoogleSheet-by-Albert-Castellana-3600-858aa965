markdown
# Component Name: FetchLastTweets

## Description

FetchLastTweets is a Yeager component that retrieves the last tweet of a list of Twitter handles. It does this by interacting with Twitter's API using the Tweepy library. The component utilizes OAuth for authentication and returns a list of last tweets corresponding to each supplied Twitter handle.

## Input and Output Models

### Input Model: `FetchLastTweetsInputDict`

The input model takes two fields:

1. `twitter_handles`: A list of Twitter handles as strings.
2. `twitter_credentials`: An instance of the `TwitterCredentials` model.

### Output Model: `FetchLastTweetsOutputDict`

The output model returns one field:

1. `last_tweets`: A list of dictionaries containing the Twitter handle and its corresponding last tweet.

### Validation and Serialization

Input and output models utilize Pydantic's `BaseModel` for validation and serialization.

## Parameters

The component accepts the following parameter:

- `args`: An instance of the `FetchLastTweetsInputDict` input model.

## Transform Function

The `transform()` method implements the following steps:

1. Prepare OAuth authentication using the provided Twitter API credentials from the `args` parameter.
2. Instantiate the Tweepy API with the configured authentication.
3. Iterate over the list of `twitter_handles` and fetch their last tweets using the `api.user_timeline()` method.
4. Append each handle and its corresponding last tweet to the `last_tweets` list.
5. Return an instance of `FetchLastTweetsOutputDict` containing the `last_tweets` list.

## External Dependencies

The component relies on the following external libraries:

1. `os`: For loading environment variables.
2. `dotenv`: For reading `.env` files to load environment variables.
3. `tweepy`: To interact with Twitter's API.
4. `fastapi`: To create and manage the API endpoint for the component.
5. `pydantic`: For input and output data validation and serialization.
6. `typing`: For defining custom types.

## API Calls

The component makes use of the following Twitter API call:

- `user_timeline()`: To fetch the last tweets from the provided list of Twitter handles.

## Error Handling

The component does not have any specific error handling implemented. It relies on the error handling provided by the Tweepy library and will raise any exceptions encountered during API calls.

## Examples

### Example 1: Fetch last tweets from a list of Twitter handles

To use the component in a Yeager Workflow, the following steps can be performed:

1. Prepare the input data containing a list of Twitter handles and Twitter API credentials.
2. Create an instance of the `FetchLastTweets` class.
3. Call the `transform()` method on the instance with the prepared input data.
4. Obtain the last tweets as a list of dictionaries.

Sample usage:

