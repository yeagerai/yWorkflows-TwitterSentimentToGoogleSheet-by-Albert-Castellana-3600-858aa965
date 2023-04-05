
# TwitterSentimentToGoogleSheet

This workflow takes a list of Twitter handles, fetches their last posts using the Twitter API, performs sentiment analysis on these posts using the TextBlob library, and creates a Google Sheet with the handle, the tweet, and its sentiment. It requires the following steps: 1. Fetch the last tweet for each handle; 2. Analyze the sentiment of the retrieved tweets; 3. Authenticate to Google Sheets API; 4. Create a new Google Sheet; 5. Write the data into the Google Sheet.
## Initial generation prompt
a workflow that takes a list of twitter handles and creates a google sheet with their last post's sentiment

## Authors: 
- yWorkflows
- Albert Castellana#3600
        