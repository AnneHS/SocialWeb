import platform
import sys
assert sys.version_info >= (3, 6)
import twitter
import json
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
response = urllib.request.urlopen()

CONSUMER_KEY = 'kKEOC6n2BKBVsks5RH45BmiRw'
CONSUMER_SECRET = 'rXrfijW6S2wxb4Mt4yVil36QDcZNawsotjBb8X9PQ2zejmX6mr'


# to get the oauth credential you need to click on the 'Generate access token' button:
OAUTH_TOKEN = '1225147204739964929-obkKVb4GndaWd3GnZY6aCLafFPtbD7'
OAUTH_TOKEN_SECRET = '7xNKPaSPQHfMzPeiD8JIemKg8dCQOBa3jp4Tx0922GGNP'
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)
print(twitter_api)

NYC_WOE_ID = 2459115
nyc_trends = twitter_api.trends.place(_id=NYC_WOE_ID)
print(nyc_trends)

# search for tweets include domino's
# search_word = 'domino\'s'
# count = 1000
# search_results = twitter_api.search.tweets(q=search_word, count=count)
# statuses = search_results['statuses']
# # print(type(statuses))
# print(json.dumps(statuses[0], ident=1))
