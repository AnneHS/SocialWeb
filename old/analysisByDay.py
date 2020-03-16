import pandas as pd
import datetime
import matplotlib.pyplot as plt


# change week and filename here
week = 'week1'
fileName = 'week1(24_01)dominos_data.csv'
# read file
filePath = '..//data//' + week + '//' + fileName
rawData = pd.read_csv(filePath, sep=';')
data = rawData

# set time to weekdays - Monday to Friday
date = data['time']
for i in range(len(date)):
    dt = date[i][:10]
    year, month, day = (int(x) for x in dt.split('-'))
    ans = datetime.date(year, month, day)
    data['time'][i] = ans.strftime("%A")


# Analysis sentiment trend - already had in 'analysis.py'
# overall trend: 1-positive, -1-negative, 0-neutral
# plt.figure(figsize=(3, 6), dpi=100)
# cats = ['1', '-1', '0']
# dominos1 = dominos1.sort_values('sentiment')
# sentiment = dominos1['sentiment']
# plt.hist(sentiment, bins=13)
# plt.ylabel('Number of tweets', fontsize=13)
# plt.show()

# number of tweets send each day
plt.figure(figsize=(8, 6), dpi=100)
cats = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
data['time'] = pd.Categorical(data['time'], categories=cats, ordered=True)
data = data.sort_values('time')
weekday = data['time']
plt.hist(weekday, bins=13)
plt.ylabel('Number of tweets', fontsize=13)
plt.show()


# number of positive tweets send each day
positive_tweet = data.loc[data['sentiment'] == 1]
plt.figure(figsize=(8, 6), dpi=100)
cats = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
positive_tweet['time'] = pd.Categorical(positive_tweet['time'], categories=cats, ordered=True)
positive_tweet = positive_tweet.sort_values('time')
pos_weekday = positive_tweet['time']
plt.hist(pos_weekday, bins=13)
plt.ylabel('Number of positive tweets', fontsize=13)
plt.show()


# number of negative tweets send each day
negative_tweet = data.loc[data['sentiment'] == -1]
plt.figure(figsize=(8, 6), dpi=100)
cats = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
negative_tweet['time'] = pd.Categorical(negative_tweet['time'], categories=cats, ordered=True)
negative_tweet = negative_tweet.sort_values('time')
nega_weekday = negative_tweet['time']
plt.hist(nega_weekday, bins=13)
plt.ylabel('Number of negative tweets', fontsize=13)
plt.show()

