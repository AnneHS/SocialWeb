import pandas as pd
import datetime
import matplotlib.pyplot as plt

# read file
file = "./week1_data/week1dominos_data.csv"
dominos1 = pd.read_csv(file, sep='\t')

# set time to weekdays - Monday to Friday
date = dominos1['time']
for i in range(len(date)):
    dt = date[i][:10]
    year, month, day = (int(x) for x in dt.split('-'))
    ans = datetime.date(year, month, day)
    dominos1['time'][i] = ans.strftime("%A")

# analysis sentiment trend
# overall trend: 1-positive, -1-negative, 0-neutral
# TODO detail trend: could add score details and plot
plt.figure(figsize=(3, 6), dpi=100)
cats = ['1', '-1', '0']
dominos1 = dominos1.sort_values('sentiment')
sentiment = dominos1['sentiment']
plt.hist(sentiment, bins=13)
plt.ylabel('Number of tweets', fontsize=13)
plt.show()

# number of tweets send each day
plt.figure(figsize=(8, 6), dpi=100)
cats = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dominos1['time'] = pd.Categorical(dominos1['time'], categories=cats, ordered=True)
dominos1 = dominos1.sort_values('time')
weekday = dominos1['time']
plt.hist(weekday, bins=13)
plt.ylabel('Number of tweets', fontsize=13)
plt.show()

# number of positive tweets send each day



# number of negative tweets send each day

