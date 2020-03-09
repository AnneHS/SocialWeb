import os
import pandas as pd
import datetime
from datetime import datetime, date, time, timedelta
import matplotlib.pyplot as plt

'''
Analyze official tweets
Analyzes tweets from official account. Produces three barcharts: (i) nr. of
tweets per weekday, (ii) nr. of retweets per weekday, (iii) number of likes
per weekday

Instructions
Specify three parameters before running this file: (i) the filename of the csv-
file that contains the data of the official twitter acount, (ii) the week that
needs to be analyzed, (iii) the brand name.

The plots are saved to: ../SocialWeb/plots/weeki
'''
# parameters
fileName='testOfficial.csv'
week = 'week1' #'week2', 'week3'
brand = 'test' #pizzahut, dominos

# get csv path
filePath='..//data//' + week + '//' + fileName
fileDir = os.path.dirname(os.path.realpath('__file__'))
csvPath = os.path.join(fileDir, filePath) #'../data/test.csv')
csvPath = os.path.abspath(os.path.realpath(csvPath))
print(csvPath)

# where to save the plots
filePath='..//plots//' + week
fileDir = os.path.dirname(os.path.realpath('__file__'))
plotPath = os.path.join(fileDir, filePath) #'../data/test.csv')
plotPath = os.path.abspath(os.path.realpath(plotPath))

# NUMBER OF TWEETS PER WEEKDAY
df = pd.read_csv(csvPath)
dates = df['Time']
weekday=[]
for i in range(len(dates)):
    dt = dates[i][:10]
    year, month, day = (int(x) for x in dt.split('-'))
    ans = date(year, month, day)
    weekday.append(ans.strftime("%A"))
df['Weekday']=weekday

# Plot bar chart: number of tweets for each day of the week
plt.figure(figsize=(8,6),dpi=80)
cats = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df['Weekday'] = pd.Categorical(df['Weekday'], categories=cats, ordered=True)
df = df.sort_values('Weekday')
weekday = df['Weekday']
plt.hist(weekday,bins=13)
plt.ylabel('Official tweets number',fontsize=13)
plotName = brand +'_tweetCount.png'
plt.savefig(os.path.join(plotPath, plotName))
plt.show()



# NUMBER OF RETWEETS PER WEEKDAY
Monday_retweet = 0
Tuesday_retweet = 0
Wednesday_retweet = 0
Thursday_retweet = 0
Friday_retweet = 0
Saturday_retweet = 0
Sunday_retweet = 0

retweet = df['Retweet count']
for i in range(len(weekday)):
    if weekday[i] == 'Monday':
        Monday_retweet += retweet[i]
    if weekday[i] == 'Tuesday':
        Tuesday_retweet += retweet[i]
    if weekday[i] == 'Wednesday':
        Wednesday_retweet += retweet[i]
    if weekday[i] == 'Thursday':
        Thursday_retweet += retweet[i]
    if weekday[i] == 'Friday':
        Friday_retweet += retweet[i]
    elif weekday[i] == 'Saturday':
        Saturday_retweet += retweet[i]
    else:
        Sunday_retweet += retweet[i]

retweet_count = dict()
retweet_count['Monday'] = Monday_retweet
retweet_count['Tuesday'] = Tuesday_retweet
retweet_count['Wednesday'] = Wednesday_retweet
retweet_count['Thursday'] = Thursday_retweet
retweet_count['Friday'] = Friday_retweet
retweet_count['Saturday'] = Saturday_retweet
retweet_count['Sunday'] = Sunday_retweet
print(retweet_count)

# Plot bar chart of nr. of retweets per weekday
plt.figure(figsize=(8,6),dpi=80)
plt.bar(range(len(retweet_count)), list(retweet_count.values()), align='center')
plt.xticks(range(len(retweet_count)), list(retweet_count.keys()))
plt.ylabel('Retweet count',fontsize=13)
plotName = brand +'_retweetCount.png'
plt.savefig(os.path.join(plotPath, plotName))
plt.show()
#plt.plot(list(retweet_count.keys()),list(retweet_count.values()))



# NUMBER OF LIKES PER WEEKDAY
Monday_like = 0
Tuesday_like = 0
Wednesday_like = 0
Thursday_like = 0
Friday_like = 0
Saturday_like = 0
Sunday_like = 0

like = df['Like count']
for i in range(len(weekday)):
    if weekday[i] == 'Monday':
        Monday_like += like[i]
    if weekday[i] == 'Tuesday':
        Tuesday_like += like[i]
    if weekday[i] == 'Wednesday':
        Wednesday_like += like[i]
    if weekday[i] == 'Thursday':
        Thursday_like += like[i]
    if weekday[i] == 'Friday':
        Friday_like += like[i]
    elif weekday[i] == 'Saturday':
        Saturday_like += like[i]
    else:
        Sunday_like += like[i]

like_count = dict()
like_count['Monday'] = Monday_like
like_count['Tuesday'] = Tuesday_like
like_count['Wednesday'] = Wednesday_like
like_count['Thursday'] = Thursday_like
like_count['Friday'] = Friday_like
like_count['Saturday'] = Saturday_like
like_count['Sunday'] = Sunday_like

print(like_count)

plt.figure(figsize=(8,6),dpi=80)
plt.bar(range(len(like_count)), list(like_count.values()), align='center')
plt.xticks(range(len(like_count)), list(like_count.keys()))
#plt.plot(list(like_count.keys()),list(like_count.values()))
plt.ylabel('Like count',fontsize=13)
plotName = brand +'_likeCount.png'
plt.savefig(os.path.join(plotPath, plotName))
plt.show()

# TODO: write all info to csv-file => needed for comparison