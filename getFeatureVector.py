import re

def processTweets(tweet):
	tweet=tweet.lower()
	tweet=re.sub('idi',' ',tweet)
	tweet=re.sub('.dir$',' ',tweet)
	tweet=re.sub('em',' ',tweet)
	print(tweet)



def getFeatureVector(tweets):
	featureVector=[]
	words=tweets.split(" ")
	for w in words:
		featureVector.append(w.lower())
	return featureVector

fp = open('data.txt', 'r')
line = fp.readline()



while line:
    #processedTweet = processTweets(line)

   featureVector = getFeatureVector("bu kitabi cox sevir")
   print (featureVector)
   line = fp.readline()
#end loop
fp.close()
