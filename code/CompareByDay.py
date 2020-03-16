import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np


def Analyse(week, fileName):
    # read file
    filePath = '..//data//' + week + '//' + fileName
    rawData = pd.read_csv(filePath, sep=';')
    data = rawData

    # set time to weekdays - Monday to Friday
    date = data['time']
    weekday=[]
    for i in range(len(date)):
        dt = date[i][:10]
        year, month, day = (int(x) for x in dt.split('-'))
        ans = datetime.date(year, month, day)
        weekday.append(ans.strftime("%A"))
        #data['time'][i] = ans.strftime("%A")

    # Creates dictionary for number of tweets per weekday
    tweet_count = {'Monday':0, 'Tuesday':0, 'Wednesday':0, 'Thursday':0,
                'Friday':0, 'Saturday':0, 'Sunday':0}
    for entry in weekday:
        tweet_count[entry]+=1


    # Get weekday for positive tweets
    posTweets = data.loc[data['sentiment'] == 1]
    dates = posTweets['time']
    weekday=[]
    for date in dates:
        dt=date[:10]
        year, month, day = (int(x) for x in dt.split('-'))
        ans = datetime.date(year, month, day)
        weekday.append(ans.strftime("%A"))

    # Create dictionary for nr. of positive tweets per weekday
    pos_count={'Monday':0, 'Tuesday':0, 'Wednesday':0, 'Thursday':0,
                'Friday':0, 'Saturday':0, 'Sunday':0}
    for entry in weekday:
        pos_count[entry]+=1

    # Get weekday for negative tweets
    negTweets = data.loc[data['sentiment'] == -1]
    dates = posTweets['time']
    weekday=[]
    for date in dates:
        dt=date[:10]
        year, month, day = (int(x) for x in dt.split('-'))
        ans = datetime.date(year, month, day)
        weekday.append(ans.strftime("%A"))

    # Create dictionary for nr. of negative tweets per weekday
    neg_count={'Monday':0, 'Tuesday':0, 'Wednesday':0, 'Thursday':0,
                'Friday':0, 'Saturday':0, 'Sunday':0}
    for entry in weekday:
        neg_count[entry]+=1

    return tweet_count, pos_count, neg_count

# Change week and filename here
week = 'week1'

fileNameDominos = 'week1(24_01)dominos_data.csv'
fileNamePizzaHut = 'week1(24_01)pizzahut_data.csv'


dTweets, dPos, dNeg = Analyse(week, fileNameDominos)
pTweets, pPos, pNeg = Analyse(week, fileNamePizzaHut)


# labels and xticks for bar plots
labels = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
x = np.arange(len(labels))
width=0.35

# Bar chart: nr of tweets per weekday
fig, ax = plt.subplots()
ax.bar(x-width/2, list(dTweets.values()), width, label='Dominos')#align='center')
ax.bar(x+width/2, list(pTweets.values()), width, label='Pizza Hut')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Tweets')
ax.legend()
plt.show()

#  Bar chart: nr of positive tweets per weekday
fig, ax = plt.subplots()
ax.bar(x-width/2, list(dPos.values()), width, label='Dominos')#align='center')
ax.bar(x+width/2, list(pPos.values()), width, label='Pizza Hut')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Positive Tweets')
ax.legend()
plt.show()

#  Bar chart: nr of negative tweets per weekday
fig, ax = plt.subplots()
ax.bar(x-width/2, list(dNeg.values()), width, label='Dominos')#align='center')
ax.bar(x+width/2, list(pNeg.values()), width, label='Pizza Hut')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Negative Tweets')
ax.legend()
plt.show()