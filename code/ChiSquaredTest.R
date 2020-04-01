
#Insert the observed like and retweets count per weekday and calculate the averages

#M   T   W   T   F   S   S 
weekday <- c("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
tweetCount<- c(3, 4,  2,  4,  3,  1,  2)
retweets <- c(222,207, 110,  293,124, 45,  180)
likes <- c(1487,1480,697, 1882,832,313,  891)

dominosData <- data.frame(weekday,tweetCount,retweets,likes)

dominosData$averageRT <- dominosData$retweets/dominosData$tweetCount
dominosData$AverageLikes <- dominosData$likes/dominosData$tweetCount

#M   T   W   T   F   S   S 
weekday <- c("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
tweetCount<- c(3,1,3,3,4,1,1)
retweets <- c(75,38,113,178,204,75,42)
likes <- c(518,221,694,1031,554,379,391)

pizzahutData <- data.frame(weekday,tweetCount,retweets,likes)

pizzahutData$averageRT <- pizzahutData$retweets/pizzahutData$tweetCount
pizzahutData$AverageLikes <- pizzahutData$likes/pizzahutData$tweetCount

#Do a goodness of fit test with expected distribution 1/7
expected <- rep(1/7,7)
chisq.test(pizzahutData$AverageLikes, p = expected)
chisq.test(pizzahutData$averageRT ,p = expected)
chisq.test(dominosData$AverageLikes, p = expected)
chisq.test(dominosData$averageRT ,p = expected)
