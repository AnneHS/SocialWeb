import pandas as pd
import datetime
import matplotlib.pyplot as plt

# read file
file = "../data/week123/nosentimentpizzahut_data.csv"
dominos1 = pd.read_csv(file, sep=';')
dominos_data = dominos1
# print()

# set time to weekdays - Monday to Friday
date = dominos_data['time']
for i in range(len(date)):
    dt = date[i][:10]
    year, month, day = (int(x) for x in dt.split('-'))
    ans = datetime.date(year, month, day)
    dominos_data['time'][i] = ans.strftime("%A")


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
dominos_data['time'] = pd.Categorical(dominos_data['time'], categories=cats, ordered=True)
dominos_data = dominos_data.sort_values('time')
weekday = dominos_data['time']
plt.hist(weekday, bins=13)
plt.ylabel('Number of tweets', fontsize=13)
# plt.show()

# number of positive tweets send each day
positive_tweet = dominos_data.loc[dominos_data['sentiment'] == 1]
plt.figure(figsize=(8, 6), dpi=100)
cats = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
positive_tweet['time'] = pd.Categorical(positive_tweet['time'], categories=cats, ordered=True)
positive_tweet = positive_tweet.sort_values('time')
pos_weekday = positive_tweet['time']
plt.hist(pos_weekday, bins=13)
plt.ylabel('Number of positive tweets', fontsize=13)
plt.show()


# number of negative tweets send each day
negative_tweet = dominos_data.loc[dominos_data['sentiment'] == -1]
plt.figure(figsize=(8, 6), dpi=100)
cats = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
negative_tweet['time'] = pd.Categorical(negative_tweet['time'], categories=cats, ordered=True)
negative_tweet = negative_tweet.sort_values('time')
nega_weekday = negative_tweet['time']
plt.hist(nega_weekday, bins=13)
plt.ylabel('Number of negative tweets', fontsize=13)
plt.show()


# positive VS negative tweets during a week
# Mon_pos = 0
# Tue_pos = 0
# Wed_pos = 0
# Thu_pos = 0
# Fri_pos = 0
# Sat_pos = 0
# Sun_pos = 0
#
#
# for i in range(len(dominos_data)):
#     if dominos_data['time'][i] == 'Monday':
#         Mon_pos += Mon_pos[i]
#     if dominos_data['time'][i] == 'Tuesday':
#         Tue_pos += Tue_pos[i]
#     if dominos_data['time'][i] == 'Wednesday':
#         Wed_pos += Wed_pos[i]
#     if dominos_data['time'][i] == 'Thursday':
#         Thu_pos += Thu_pos[i]
#     if dominos_data['time'][i] == 'Friday':
#         Fri_pos += Fri_pos[i]
#     elif dominos_data['time'][i] == 'Saturday':
#         Sat_pos += Sat_pos[i]
#     else:
#         Sun_pos += Sun_pos[i]
#
#
# positive_count = dict()
# positive_count['Monday'] = Mon_pos
# positive_count['Tuesday'] = Tue_pos
# positive_count['Wednesday'] = Wed_pos
# positive_count['Thursday'] = Thu_pos
# positive_count['Friday'] = Fri_pos
# positive_count['Saturday'] = Sat_pos
# positive_count['Sunday'] = Sun_pos
# print(positive_count)
# positive_data = plt.hist(pos_weekday)
# negative_data = plt.hist(nega_weekday)
# plt.figure(figsize=(8,6), dpi=100)
# plt.plot(pos_weekday, positive_data)
# # plt.legend(['positive', 'negative'])
# plt.show()