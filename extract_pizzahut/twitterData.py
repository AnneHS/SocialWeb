#!/usr/bin/env python
# coding: utf-8

# In[2]:


import platform
import sys
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


# In[37]:


import os
import tweepy as tw
import pandas as pd

auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tw.API(auth, wait_on_rate_limit=True)

search_words = 'pizzahut'
date_since = '2020-02-21'
date_until = '2020-02-27'
tweets_time = []
tweets_id = []
tweets_text = []

# for status in tw.Cursor(api.search, q=search_words, since=date_since, until=date_until).items(100):
#     print(status)
tweets = tw.Cursor(api.search, q=search_words, lang="en",since=date_since, until=date_until).items(100000)
for tweets in tweets:
    tweets_time.append(tweets.created_at)
    tweets_id.append(tweets.id)
    tweets_text.append(tweets.text)

# import json
# print(type(tweets_list))
print(tweets_time)
print(tweets_id)
print(tweets_text)


# In[38]:


import csv

rows = zip(tweets_time, tweets_id, tweets_text)
newPath = "test.csv"
with open(newPath, "w") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
