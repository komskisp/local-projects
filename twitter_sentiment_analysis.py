from textblob import TextBlob
import tweepy



api_key = 'you_twitter_api_key'
api_key_secret = 'your_twitter_api_secret'

access_token = 'your_twitter_token_access'
access_token_secret = 'your_twitter_token_secret'

auth = tweepy.AppAuthHandler(api_key, api_key_secret)


api = tweepy.API(auth, wait_on_rate_limit=True,
wait_on_rate_limit_notify=True)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)



  





