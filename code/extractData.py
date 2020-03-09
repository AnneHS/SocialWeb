
import os
import tweepy as tw
import pandas as pd
import platform
import sys
import twitter
import csv
from pathlib import Path

print("This computer is running on Python " + platform.python_version())
assert sys.version_info >= (3, 6)

# parameters
search_words = 'pizzahut' #pizzahut, dominos
date_since = '2020-03-08'
date_until = '2020-03-09'
week= 'week1' #'week2', 'week3'
csvName='..//data//' + week + '//test.csv'

# csv path
fileDir=fileDir = os.path.dirname(os.path.realpath('__file__'))
csvPath = os.path.join(fileDir, csvName) #'../data/test.csv')
csvPath = os.path.abspath(os.path.realpath(csvPath))
print(csvPath)

# keys & tokens
CONSUMER_KEY = 'kKEOC6n2BKBVsks5RH45BmiRw'
CONSUMER_SECRET = 'rXrfijW6S2wxb4Mt4yVil36QDcZNawsotjBb8X9PQ2zejmX6mr'
OAUTH_TOKEN = '1225147204739964929-obkKVb4GndaWd3GnZY6aCLafFPtbD7'
OAUTH_TOKEN_SECRET = '7xNKPaSPQHfMzPeiD8JIemKg8dCQOBa3jp4Tx0922GGNP'
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)
print(twitter_api)

#
auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tw.API(auth, wait_on_rate_limit=True)

# extract data
tweets_time = []
tweets_id = []
tweets_text = []
tweets = tw.Cursor(api.search, q=search_words, lang="en",since=date_since, until=date_until).items(100000)
for tweets in tweets:
    tweets_time.append(tweets.created_at)
    tweets_id.append(tweets.id)
    tweets_text.append(tweets.text)

# print
print(tweets_time)
print(tweets_id)
print(tweets_text)
rows = zip(tweets_time, tweets_id, tweets_text)

#newPath = test.csv
with open(csvPath, "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
