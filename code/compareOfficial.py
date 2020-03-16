import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
Compare Dominos and PizzaHut
Compares the results of the analysis for the official Twitter accounts. Creates
3 barplots to show the number of tweets, retweets and likes for a given week.

Instructions
Specify 3 parameters before running this files
    (i) week
    (ii) name of Dominos csv-file (results analysis official account)
    (iii) name of PizzaHut csv-file (results analysis official account)

The plots are saved to: ../SocialWeb/plots/weeki
'''

# parameters
week = 'week1' #'week2', 'week3'
dominosFile = 'dominos_analysis_week1.csv'
pizzahutFile='pizzahut_analysis_week1.csv'

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

# labels and xticks for bar plots
labels = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
x = np.arange(len(labels))
width=0.35

# Where to save the plots
filePath='..//plots//' + week
fileDir = os.path.dirname(os.path.realpath('__file__'))
plotPath = os.path.join(fileDir, filePath) #'../data/test.csv')
plotPath = os.path.abspath(os.path.realpath(plotPath))

# nr of tweets
fig, ax = plt.subplots()
ax.bar(x-width/2, list(dTweets.values()), width, label='Dominos')#align='center')
ax.bar(x+width/2, list(pTweets.values()), width, label='Pizza Hut')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Tweets')
ax.legend()
plotName = 'OfficialTweetsComparison_' + week + '.png'
plt.savefig(os.path.join(plotPath, plotName))
plt.show()

# nr of retweets
fig, ax = plt.subplots()
ax.bar(x-width/2, list(dRetweets.values()), width, label='Dominos')#align='center')
ax.bar(x+width/2, list(pRetweets.values()), width, label='Pizza Hut')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Retweets')
ax.legend()
plotName = 'OfficialRetweetsComparison_' + week + '.png'
plt.savefig(os.path.join(plotPath, plotName))
plt.show()

# nr of retweets
fig, ax = plt.subplots()
ax.bar(x-width/2, list(dLikes.values()), width, label='Dominos')#align='center')
ax.bar(x+width/2, list(pLikes.values()), width, label='Pizza Hut')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Likes')
ax.legend()
plotName = 'OfficialLikesComparison_' + week + '.png'
plt.savefig(os.path.join(plotPath, plotName))
plt.show()

#TODO: SAVE PLOTS
