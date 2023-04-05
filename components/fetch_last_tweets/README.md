
# FetchLastTweets

This component receives the list of Twitter handles and the TwitterCredentials. It uses the Tweepy library to fetch the last tweet from each handle and returns a list of dictionaries with the format {'handle': handle, 'tweet': last_tweet}. Inputs come from the Workflow InitialData.

## Initial generation prompt
description: 'This component receives the list of Twitter handles and the TwitterCredentials.
  It uses the Tweepy library to fetch the last tweet from each handle and returns
  a list of dictionaries with the format {''handle'': handle, ''tweet'': last_tweet}.
  Inputs come from the Workflow InitialData.'
name: FetchLastTweets


## Transformer breakdown
- Initialize and authenticate Tweepy with TwitterCredentials
- For each handle in the list of Twitter_handles:
- Fetch the latest tweet using Tweepy
- Add the handle and tweet to the output list (in dictionary format)

## Parameters
[]

        