
# TwitterSentimentToGoogleSheet

This component retrieves the sentiment analysis of tweets from specified Twitter handles, using given Twitter credentials, and stores the result in a newly created Google Sheet which URL is provided as output.

## Initial generation prompt
description: "IOs - 'Inputs: TwitterHandles (list of strings), TwitterCredentials\
  \ (dict containing API\n  key and secret); Outputs: GoogleSheetURL (string containing\
  \ the URL of the created\n  Google Sheet)'\n"
name: TwitterSentimentToGoogleSheet


## Transformer breakdown
- Retrieve tweets from specified Twitter handles using the TwitterCredentials
- Perform sentiment analysis on the retrieved tweets
- Create a new Google Sheet
- Store sentiment analysis results in the Google Sheet
- Return the Google Sheet URL as output

## Parameters
[]

        