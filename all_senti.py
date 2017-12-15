
import csv
import nltk
import re

def processTweet(tweet):
	tweet=tweet.lower()
	#tweet=re.sub('idi',' ',tweet)
	tweet=re.sub('dir',' ',tweet)
	#tweet=re.sub('em',' ',tweet)
	return tweet

def getFeatureVector(tweet):
	
	featureVector=[]
	


	words=tweet.split(" ")
	
	
	for w in words:
	
		featureVector.append(w.lower())
	return featureVector

def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in featureList:
        features['contains(%s)' % word] = (word in tweet_words)
    return features






inputTweets=csv.reader(open('data.csv','r'),delimiter=";")
featureList=[]

tweets=[]
for row in inputTweets:
	tweet=row[0]
	sentiment=row[2]
	
	
	
	processedTweet=processTweet(tweet)
	
	featureVector=getFeatureVector(processedTweet)
	featureList.extend(featureVector)

	tweets.append((featureVector,sentiment))


featureList=list(set(featureList))
#print(featureList)

training_set=nltk.classify.util.apply_features(extract_features,tweets)
#print(training_set)
NBClassifier=nltk.NaiveBayesClassifier.train(training_set)

testTweet='gozumuzu qorxudursan'
processed=processTweet(testTweet)
#print(extract_features(processed))
result=NBClassifier.classify(extract_features(getFeatureVector(processed)))
print(result)




















