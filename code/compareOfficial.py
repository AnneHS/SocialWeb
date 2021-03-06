import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
Compare Dominos and PizzaHut
Compares the results of the analysis for the official Twitter accounts. Creates
3 barplots to show the number of tweets, retweets and likes per weekday, for both
Dominoz and Pizzahut, over a given period.

Instructions
Specify 1 parameter to run this file:
    (i) the weeks parameter should include all weeks that you want to include
            for the comparison (e.g. weeks = ['week1', 'week2'])

The plots are saved to: ../SocialWeb/plots/overall
'''

# parameter
weeks = ['week1', 'week2', 'week3', 'week4']

# to keep track of overall Dominos data
dominosTweets = {'Monday': 0, 'Tuesday': 0, 'Wednesday':0, 'Thursday':0, 'Friday':0, 'Saturday':0, 'Sunday':0}
dominosRetweets = {'Monday': 0, 'Tuesday': 0, 'Wednesday':0, 'Thursday':0, 'Friday':0, 'Saturday':0, 'Sunday':0}
dominosLikes = {'Monday': 0, 'Tuesday': 0, 'Wednesday':0, 'Thursday':0, 'Friday':0, 'Saturday':0, 'Sunday':0}

# to keep track of overall PizzaHut data
pizzahutTweets = {'Monday': 0, 'Tuesday': 0, 'Wednesday':0, 'Thursday':0, 'Friday':0, 'Saturday':0, 'Sunday':0}
pizzahutRetweets = {'Monday': 0, 'Tuesday': 0, 'Wednesday':0, 'Thursday':0, 'Friday':0, 'Saturday':0, 'Sunday':0}
pizzahutLikes = {'Monday': 0, 'Tuesday': 0, 'Wednesday':0, 'Thursday':0, 'Friday':0, 'Saturday':0, 'Sunday':0}

for week in weeks:
    dominosFile= 'dominos_analysis_' + week + '.csv'
    pizzahutFile='pizzahut_analysis_'+ week + '.csv'

    # read dominos csv
    filePath='..//data//' + week + '//' + dominosFile
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    csvPath = os.path.join(fileDir, filePath) #'../data/test.csv')
    csvPath = os.path.abspath(os.path.realpath(csvPath))
    dominos_df = pd.read_csv(csvPath, index_col=0)

    # read pizahut csv
    filePath='..//data//' + week + '//' + pizzahutFile
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    csvPath = os.path.join(fileDir, filePath) #'../data/test.csv')
    csvPath = os.path.abspath(os.path.realpath(csvPath))
    pizzahut_df = pd.read_csv(csvPath, index_col=0)

    # dominos data
    dominosDict = dominos_df.to_dict(orient='index')
    dTweets = dominosDict['Tweets']
    dRetweets = dominosDict['Retweets']
    dLikes = dominosDict['Likes']

    # pizzahut data
    pizzahutDict = pizzahut_df.to_dict(orient='index')
    pTweets = pizzahutDict['Tweets']
    pRetweets= pizzahutDict['Retweets']
    pLikes = pizzahutDict['Likes']

    # Merge with dominos data of previous weeks
    dominosTweets={key: dominosTweets.get(key, 0) + dTweets.get(key, 0)
          for key in dominosTweets}
    dominosRetweets={key: dominosRetweets.get(key, 0) + dRetweets.get(key, 0)
          for key in dominosRetweets}
    dominosLikes={key: dominosLikes.get(key, 0) + dLikes.get(key, 0)
          for key in dominosLikes}

    # Merge with PizzaHut data of previous weeks
    pizzahutTweets={key: pizzahutTweets.get(key, 0) + pTweets.get(key, 0)
          for key in pizzahutTweets}
    pizzahutRetweets={key: pizzahutRetweets.get(key, 0) + pRetweets.get(key, 0)
          for key in pizzahutRetweets}
    pizzahutLikes={key: pizzahutLikes.get(key, 0) + pLikes.get(key, 0)
          for key in pizzahutLikes}# | set(pLikes)}

# Where to save the plots
filePath='..//plots//overall'
fileDir = os.path.dirname(os.path.realpath('__file__'))
plotPath = os.path.join(fileDir, filePath) #'../data/test.csv')
plotPath = os.path.abspath(os.path.realpath(plotPath))

# labels and xticks for bar plots
labels = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
x = np.arange(len(labels))
width=0.35

# nr of tweets
fig, ax = plt.subplots()
ax.bar(x-width/2, list(dominosTweets.values()), width, label='Dominos')#align='center')
ax.bar(x+width/2, list(pizzahutTweets.values()), width, label='Pizza Hut')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Tweets')
ax.legend()
plotName = 'Overall_OfficialTweetsComparison.png'
plt.savefig(os.path.join(plotPath, plotName))
plt.show()

# nr of retweets
fig, ax = plt.subplots()
ax.bar(x-width/2, list(dominosRetweets.values()), width, label='Dominos')#align='center')
ax.bar(x+width/2, list(pizzahutRetweets.values()), width, label='Pizza Hut')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Retweets')
ax.legend()
plotName = 'Overall_OfficialRetweetsComparison.png'
plt.savefig(os.path.join(plotPath, plotName))
plt.show()

# nr of likes
fig, ax = plt.subplots()
ax.bar(x-width/2, list(dominosLikes.values()), width, label='Dominos')#align='center')
ax.bar(x+width/2, list(pizzahutLikes.values()), width, label='Pizza Hut')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Likes')
ax.legend()
plotName = 'Overall_OfficialLikesComparison.png'
plt.savefig(os.path.join(plotPath, plotName))
plt.show()
