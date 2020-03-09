import os
import re
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from textblob import TextBlob

'''
Sentiment analysis of PizzaHut csv using textblob
'''

# parameters: csv filename + csv folder
fileName= 'test.csv'  #'week1(24_01)dominos_data.csv'
week = 'week1'

# get csv path
filePath='..//data//' + week + '//' + fileName
fileDir = os.path.dirname(os.path.realpath('__file__'))
csvPath = os.path.join(fileDir, filePath) #'../data/test.csv')
csvPath = os.path.abspath(os.path.realpath(csvPath))
print(csvPath)

# read tweet text
data = pd.read_csv(csvPath, engine='python', names=['time', 'id', 'text'], header=None)
tweetText = data['text']


def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def get_tweet_sentiment(tweet):
    analysis = TextBlob(tweet)
    # set sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'


def analysis(tweets):
    count = 0
    tweetsList = []

    for tweet in tweets:
        parsed_tweet = {}

        # clean tweet
        cl_tweet = clean_tweet(tweet)
        parsed_tweet['text'] = cl_tweet

        # get sentiment
        sentiment=get_tweet_sentiment(cl_tweet)
        parsed_tweet['sentiment']=sentiment

        tweetsList.append(parsed_tweet)

    return tweetsList

def plot_sentiment(tweetText, tweets):
    '''
    Plot histogram for polarity score and bar plot for the sentiment analysis
    categorization (positive, neutral, negative)
    '''

    # Clean & get sentiment values
    cleaned_tweets = [clean_tweet(tweet) for tweet in tweetText]
    sentiment_objects = [TextBlob(tweet) for tweet in cleaned_tweets]
    sentiment_values = [[tweet.sentiment.polarity, str(tweet)] for tweet in sentiment_objects]

    # Dataframe
    sentiment_df = pd.DataFrame(sentiment_values, columns=["polarity", "tweet"])
    sentiment_df.head()

    # where to save the plots
    filePath='..//plots//' + week
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    plotPath = os.path.join(fileDir, filePath) #'../data/test.csv')
    plotPath = os.path.abspath(os.path.realpath(plotPath))


    # Plot histogram of the polarity values
    fig, ax = plt.subplots(figsize=(8, 6))
    sentiment_df.hist(bins=[-1, -0.75, -0.5, -0.25, 0.25, 0.5, 0.75, 1],
                 ax=ax,
                 color="purple")

    plt.title("Sentiments from Tweets on Pizza Hut")
    plotName = 'polarity.png'
    plt.savefig(os.path.join(plotPath, plotName))
    plt.show()

    # Plot barplot of sentiment analysis 
    categorized_tweets = [tweet['sentiment'] for tweet in tweets]
    categorie_counts = Counter(categorized_tweets)
    df = pd.DataFrame.from_dict(categorie_counts, orient='index')
    df.plot(kind='bar')
    plotName = 'sentiment.png'
    plt.savefig(os.path.join(plotPath, plotName))
    plt.show()


# Sentiment analysis
tweets=analysis(tweetText)

print('Number of tweets: {} '.format(len(tweets)))
# percentage of positive tweets
ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))

# percentage of negative tweets
ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))

# percentage of neutral tweets
print("Neutral tweets percentage: {} %".format(100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets)))

# printing first 5 positive tweets
print("\n\nPositive tweets:")
for tweet in ptweets[:10]:
    print(tweet['text'])

# printing first 5 negative tweets
print("\n\nNegative tweets:")
for tweet in ntweets[:10]:
    print(tweet['text'])

# Plot sentiment analysis
plot_sentiment(tweetText, tweets)
