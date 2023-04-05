
# AnalyzeSentiments

This component receives the list of dictionaries from FetchLastTweets, uses the TextBlob library to analyze the sentiment and appends the sentiment to each dictionary with the format {'handle': handle, 'tweet': last_tweet, 'sentiment': sentiment_score}.

## Initial generation prompt
description: 'This component receives the list of dictionaries from FetchLastTweets,
  uses the TextBlob library to analyze the sentiment and appends the sentiment to
  each dictionary with the format {''handle'': handle, ''tweet'': last_tweet, ''sentiment'':
  sentiment_score}.'
name: AnalyzeSentiments


## Transformer breakdown
- Load tweets_list
- For each tweet in tweets_list:
- Extract handle and tweet content
- Use TextBlob to analyze the tweet's sentiment
- Append sentiment score to the dictionary as 'sentiment'
- Add updated dictionary to resulting sentiments_list

## Parameters
[]

        