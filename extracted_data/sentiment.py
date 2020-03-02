import csv
import re
import pandas as pd
from textblob import TextBlob

'''
Sentiment analysis of PizzaHut csv using textblob
'''
data = pd.read_csv('21_27_pizzahut_data.csv', engine='python', names=['time', 'id', 'text'], header=None)
tweetText = data['text']
print(tweetText)
sentiment_list = []


def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def get_tweet_sentiment(tweet):
    analysis = TextBlob(tweet)
    # set sentiment
    if analysis.sentiment.polarity > 0:
        sentiment_list.append(1)
    elif analysis.sentiment.polarity == 0:
        sentiment_list.append(0)
    else:
        sentiment_list.append(-1)


def analysis(tweets):
    count = 0
    tweetsList = []

    for tweet in tweets:
        parsed_tweet = {}

        # clean tweet
        cl_tweet = clean_tweet(tweet)
        parsed_tweet['text'] = cl_tweet

        # get sentiment
        sentiment = get_tweet_sentiment(cl_tweet)
        parsed_tweet['sentiment'] = sentiment

        tweetsList.append(parsed_tweet)

    return tweetsList


tweets = analysis(tweetText)
data['sentiment'] = sentiment_list

with open("sentiment_analysis.csv", 'w') as write_csv:
    write_csv.write(data.to_csv(sep='\t', index=False))


# # percentage of positive tweets
# ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
# print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))
#
# # percentage of negative tweets
# ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
# print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))
#
# # percentage of neutral tweets
# print("Neutral tweets percentage: {} %".format(100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets)))
#
# # printing first 5 positive tweets
# print("\n\nPositive tweets:")
# for tweet in ptweets[:10]:
#     print(tweet['text'])
#
# # printing first 5 negative tweets
# print("\n\nNegative tweets:")
# for tweet in ntweets[:10]:
#     print(tweet['text'])
