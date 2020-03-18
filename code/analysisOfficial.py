import os
import pandas as pd
import datetime
from datetime import datetime, date, time, timedelta
import matplotlib.pyplot as plt

'''
Analyze official tweets
Analyzes tweets from official account. Produces a csv-file with (i) nr. of
tweets per weekday, (ii) nr. of retweets per weekday, (iii) nr of likes
per weekday, which is stored in the data folder for the corresponding week.

Instructions
Specify four parameters before running this file:
    (i) the filename of the csv-file that contains the data of the official
        twitter acount;
    (ii) the week for which you want to run the analysis;
    (iii) the brand name ('pizzahut', 'dominos')
    (iv) the name of the CSV output file.

The csv file is saved to: ../SocialWeb/data/weeki
'''
# parameters
fileName=  'DominosOfficial(09_03_15_03).csv'   #'DominosOfficial24-02_01-03.csv' , 'PizzaHutOfficial24-02_01-03.csv'
week = 'week3' #'week1', 'week3'
brand = 'dominos' #pizzahut, dominos
outputName = brand + '_analysis_'+ week + '.csv'

# get csv path
filePath='..//data//' + week + '//' + fileName
fileDir = os.path.dirname(os.path.realpath('__file__'))
csvPath = os.path.join(fileDir, filePath) #'../data/test.csv')
csvPath = os.path.abspath(os.path.realpath(csvPath))

# get data
rawData = pd.read_csv(csvPath, delimiter = ';')
rawData.columns=['Time','Post_id','Tweet','Retweet count','Like count'] # needed because some of the older csv-files don't have header
df=rawData.dropna() # drop NaN rows (;;;)

# Get day of the week for each tweet
dates = df['Time']
weekday=[]
for ts in dates:
    dt=ts[:10]
    year, month, day = (int(x) for x in dt.split('-'))
    ans = date(year, month, day)
    weekday.append(ans.strftime("%A"))
    #print(weekday)
df['Weekday']=weekday.copy()


# 1. TNUMBER OF TWEETS PER WEEKDAT
tweet_count = {'Monday':0, 'Tuesday':0, 'Wednesday':0, 'Thursday':0,
            'Friday':0, 'Saturday':0, 'Sunday':0}
for entry in weekday:
    tweet_count[entry]+=1
weekday = df['Weekday']


# 2. NUMBER OF RETWEETS PER WEEKDAY
retweet_count = {'Monday':0, 'Tuesday':0, 'Wednesday':0, 'Thursday':0,
            'Friday':0, 'Saturday':0, 'Sunday':0}

retweet = df['Retweet count']
for counter, day in enumerate(weekday):
    i=weekday.index[counter]
    retweet_count[day]+= retweet[i]


# 3. NUMBER OF LIKES PER WEEKDAY
like_count = {'Monday':0, 'Tuesday':0, 'Wednesday':0, 'Thursday':0,
            'Friday':0, 'Saturday':0, 'Sunday':0}

like = df['Like count']
for counter, day in enumerate(weekday):
    i=weekday.index[counter]
    like_count[day]+= like[i]


# Save dictionaries to csv
# Dictionary for analysis: nr. of tweets, retweets and likes for each weekday
index_list=['Tweets', 'Retweets', 'Likes']
df=pd.DataFrame([tweet_count, retweet_count, like_count], columns=retweet_count.keys())
df.index=index_list
df.to_csv()
print(csvPath)

# Get csv path: where data is stored
filePath='..//data//' + week + '//' + outputName
fileDir = os.path.dirname(os.path.realpath('__file__'))
csvPath = os.path.join(fileDir, filePath) #'../data/test.csv')
csvPath = os.path.abspath(os.path.realpath(csvPath))

# Create csv
df.to_csv(csvPath)
