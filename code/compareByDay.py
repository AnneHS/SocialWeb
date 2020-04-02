import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
import os

'''
Compare Dominos and Pizzahut at each day of a given week. Creats 3 barcharts:
(i) Nr. of Tweets per day;
(ii) Nr. of positive Tweets per day;
(iii) Nr. of negative Tweets per day.

Instructions
Specify 3 parameters before running this script:
(i) week (e.g. 'week1');
(ii) name of Dominos csv-file;
(iii) name of Pizzahut csv-file;
where the csv-files already contain the sentiment info.

The plots are saved to: ../SocialWeb/plots/weeki
'''

def Analyse(week, fileName):
    # read file
    print(fileName)
    filePath = '..//data//' + week + '//' + fileName
    if fileName != 'week3(09_15)pizzahut_data.csv':
        df = pd.read_csv(filePath, delimiter=';', error_bad_lines=False)
        #df.columns=['time','id','text','sentiment']
    else:
        df = pd.read_csv(filePath, error_bad_lines=False, engine='python')
        for entry in df:
            print(entry)

    print(df.columns.values.tolist())
    data = df

    # set time to weekdays - Monday to Friday
    date = data['time']
    weekday=[]
    for i in range(len(date)):
        dt = date[i][:10]
        year, month, day = (int(x) for x in dt.split('-'))
        ans = datetime.date(year, month, day)
        weekday.append(ans.strftime("%A"))

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
    dates2 = negTweets['time']
    weekday=[]
    for date in dates2:
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
# Parameters
week = 'week4'
fileNameDominos = 'week4(16_22)dominos_data.csv'
fileNamePizzaHut = 'week4(16_22)pizzahut_data.csv'


# Get Tweet nfo
dTweets, dPos, dNeg = Analyse(week, fileNameDominos)
pTweets, pPos, pNeg = Analyse(week, fileNamePizzaHut)

# Where to save the plots
filePath='..//plots//' + week
fileDir = os.path.dirname(os.path.realpath('__file__'))
plotPath = os.path.join(fileDir, filePath) #'../data/test.csv')
plotPath = os.path.abspath(os.path.realpath(plotPath))

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
plotName = 'TweetsByDay_' + week + '.png'
plt.savefig(os.path.join(plotPath, plotName))
plt.show()

# Bar chart: nr of positive tweets per weekday
fig, ax = plt.subplots()
ax.bar(x-width/2, list(dPos.values()), width, label='Dominos')#align='center')
ax.bar(x+width/2, list(pPos.values()), width, label='Pizza Hut')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Positive Tweets')
ax.legend()
plotName = 'PosByDay_' + week + '.png'
plt.savefig(os.path.join(plotPath, plotName))
plt.show()

# Bar chart: nr of negative tweets per weekday
fig, ax = plt.subplots()
ax.bar(x-width/2, list(dNeg.values()), width, label='Dominos')#align='center')
ax.bar(x+width/2, list(pNeg.values()), width, label='Pizza Hut')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Negative Tweets')
ax.legend()
plotName = 'NegByDay_' + week + '.png'
plt.savefig(os.path.join(plotPath, plotName))
plt.show()
