import tweepy
from textblob import *

search_string=input("enter string to search")
pCount=0
nCount=0
cons_key="afdWmge3yjcUt3Qhdl13nCwVI"
cons_secret="GhJdf7hr5hqIngQVDA3r6FzAqJP7CZNNeO77njO2u966jdb8D8"

access_token="2909134638-XgQZwad8JyMs7DG0vw4ER8gSNFG5AJAjxs3STv8"
access_token_secret="2nYCvIiXzCDBJxdaDAZhhH43lIpIhk8Rj9FjggnlTz7S3"

auth=tweepy.OAuthHandler(cons_key,cons_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

public_tweets=api.search(search_string)

for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment.polarity)
    if analysis.sentiment.polarity>=0:
        pCount+=1
    else:
        nCount+=1
print("Positive:",pCount)
print("Negative:",nCount)
