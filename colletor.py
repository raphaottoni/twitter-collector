import tweepy
#import twitter dev account informaiton
from config import *


# oAuth authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

timeline = api.user_timeline(screen_name="jpesce", count=200)

while timeline:
    for tweet in timeline:
        print "lastId " +  str(tweet.id)
        lastID= tweet.id
        print tweet.id
        print tweet.created_at
        print tweet.text
    timeline = api.user_timeline(screen_name="jpesce", count=200, max_id=lastID -1)

