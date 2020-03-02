#!/usr/bin/env python
# coding: utf-8

# In[2]:

import re
import platform
import sys
import os
import tweepy as tw
import pandas as pd
import csv
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter

print("This jupyter notebook is running on Python " + platform.python_version())
# It's good practice to assert packages requirements at the beginning of a script:
assert sys.version_info >= (3, 6) # Tested with Python==3.7.5
import twitter # Tell Python to use the twitter package

CONSUMER_KEY = 'kKEOC6n2BKBVsks5RH45BmiRw'
CONSUMER_SECRET = 'rXrfijW6S2wxb4Mt4yVil36QDcZNawsotjBb8X9PQ2zejmX6mr'

# to get the oauth credential you need to click on the 'Generate access token' button:
OAUTH_TOKEN = '1225147204739964929-obkKVb4GndaWd3GnZY6aCLafFPtbD7' 
OAUTH_TOKEN_SECRET = '7xNKPaSPQHfMzPeiD8JIemKg8dCQOBa3jp4Tx0922GGNP'
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)
print(twitter_api) 


tweets_time = []
tweets_id = []
tweets_text = []
tweets_retweet_count = []
tweets_likes = []

auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tw.API(auth, wait_on_rate_limit=True)

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweet).split())

search_words = 'pizzahut'
date_since = '2020-02-21'
date_until = '2020-02-27'
tweets_time = []
tweets_id = []
tweets_text = []
account_list = ["dominos"]

if len(account_list) > 0:
    for target in account_list:
        print("Getting data for " + target)
        item = api.get_user(target)
        print("name: " + item.name)
        print("screen_name: " + item.screen_name)
        print("description: " + item.description)
        print("statuses_count: " + str(item.statuses_count))
        print("friends_count: " + str(item.friends_count))
        print("followers_count: " + str(item.followers_count))


account_created_date = item.created_at
delta = datetime.utcnow() - account_created_date
account_age_days = delta.days
print("Account age (in days): " + str(account_age_days))

#Array to hold most popular hashtags and mentions for later
hashtags = []
mentions = []
tweet_count = 0
end_date = datetime.utcnow() - timedelta(days=30)
for tweet in Cursor(api.user_timeline, id=target).items():
    if tweet.in_reply_to_status_id is None:
        #Tweet is not a reply
        #print(tweet.text)
        #print(tweet.retweet_count)
        #print(tweet.favorite_count)
        tweets_time.append(tweet.created_at)
        tweets_id.append(tweet.id)
        tweets_text.append(clean_tweet(tweet.text))
        tweets_retweet_count.append(tweet.retweet_count)
        tweets_likes.append(tweet.favorite_count)

rows = zip(tweets_time, tweets_id, tweets_text,tweets_retweet_count,tweets_likes)
newPath = "24-02_data.csv"
print('writing')
with open(newPath, "w") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
print('done')