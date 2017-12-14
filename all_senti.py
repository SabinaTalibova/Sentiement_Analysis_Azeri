
import csv
inputTweets=csv.reader(open('data.csv','r'),delimiter=',')
#featureList[]

tweets=[]
for row in inputTweets:
	sentiment=row[3]
	tweet=row[0]
	