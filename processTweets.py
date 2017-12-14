import re

def processTweets(tweet):
	tweet=tweet.lower()
	tweet=re.sub('idi',' ',tweet)
	tweet=re.sub('.dir$',' ',tweet)
	tweet=re.sub('em',' ',tweet)
	print(tweet)



	


filetoprocess=open('data.txt','r')
line=filetoprocess.readline()


while line:
	
	processed=processTweets(line)
	
	line=filetoprocess.readline()

filetoprocess.close()