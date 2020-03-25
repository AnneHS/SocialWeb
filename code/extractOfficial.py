import os
import tweepy as tw
import pandas as pd
import platform
import sys
import twitter
import csv
from pathlib import Path
from datetime import datetime, date, time, timedelta
from tweepy import Cursor
import re

'''
Extracts tweets from the official account and writes the cleaned
data to a csv-file.

Instructions: Change the parameter variables to specify the dates, the name of
the official account, the week ('week1', 'week2'  etc.) and the name of the
written csv-file.

The csv-file is saved in ../SocialWeb/data/weeki
'''

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweet).split())

# parameters
date_since = '2020-02-24'
date_until = '2020-03-23'
brand = 'pizzahut'
week = 'week4' #'week2', 'week3'
csvName = 'overallPizzahutOfficial.csv'
account_list = [brand]

# path for csv file
csvDirectory = '..//data//' + week + '//' + csvName
fileDir = os.path.dirname(os.path.realpath('__file__'))
csvPath = os.path.join(fileDir, csvDirectory) #'../data/test.csv')
csvPath = os.path.abspath(os.path.realpath(csvPath))
print(csvPath)

# keys & tokens
CONSUMER_KEY = 'kKEOC6n2BKBVsks5RH45BmiRw'
CONSUMER_SECRET = 'rXrfijW6S2wxb4Mt4yVil36QDcZNawsotjBb8X9PQ2zejmX6mr'
OAUTH_TOKEN = '1225147204739964929-obkKVb4GndaWd3GnZY6aCLafFPtbD7'
OAUTH_TOKEN_SECRET = '7xNKPaSPQHfMzPeiD8JIemKg8dCQOBa3jp4Tx0922GGNP'

# twitter api
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)
print(twitter_api)

auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tw.API(auth, wait_on_rate_limit=True)

# print account info
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

# csv columns
tweets_time = ['Time',]
tweets_id = ['Post_id',]
tweets_text = ['Tweet',]
tweets_retweet_count = ['Retweet count',]
tweets_likes = ['Like count']

# extract data
hashtags = [] # currently not used
mentions = [] # currently not used
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

# write to csv
print('writing')
with open(csvPath, "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
print('done')
