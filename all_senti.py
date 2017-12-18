
import csv
import nltk
import re
from tkinter import *
import time
#import tkfont 
from tkinter import font



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







def featurelistAndArray():
    featureList=[]
    inputTweets=csv.reader(open('data.csv','r'),delimiter=",")


    tweets=[]
    for row in inputTweets:
	    tweet=row[0]
	    sentiment=row[2]
	
	
	    processedTweet=processTweet(tweet)
	 
	    featureVector=getFeatureVector(processedTweet)
	    featureList.extend(featureVector)

	    tweets.append((featureVector,sentiment))


    featureList=list(set(featureList))
    return (featureList,tweets)
featureList=featurelistAndArray()[0]
tweets=featurelistAndArray()[1]


def show():
    top = Tk()
    RTitle=top.title("Sentiment analyzer")
    RWidth=top.winfo_screenwidth()/2
    RHeight=top.winfo_screenheight()/2
    top.geometry("%dx%d+0+0" % (RWidth, RHeight))


    L1 = Label(top, text="Enter the sentnce you want to check",font=("Helvetica", 20))
    L1.place(x=90, y=50)
    E1 = Entry(top, bd =3)
    E1.place(x=130, y=150,width=400,height=50)
    def get():
    	testTweet=E1.get()
    	processed=processTweet(testTweet)
    	training_set=nltk.classify.util.apply_features(extract_features,tweets)
    	NBClassifier=nltk.NaiveBayesClassifier.train(training_set)
    	result=NBClassifier.classify(extract_features(getFeatureVector(processed)))
    	

    	result_font=font.Font(family='Helvetica',size=18)
    	if result=='positive':
    	    L3=Label(top,text=result,fg='green',font=result_font)
    	elif result=='negative':
    	    L3=Label(top,text=result,fg='red',font=result_font)
    	L3.place(x=500,y=300)
    	L2=Label(top,text="Sentiment of the sentence you included is: ",font=result_font)
    	L2.place(x=20,y=300)
    	
    	

    button_font=font.Font(family='Helvetica',size=25)

    B1=Button(top,text="Check",command=get,bg='green',fg='white',font=button_font,activeforeground='green')
    B1.place(x=250, y=200,width=150,height=50)

    top.mainloop() 

show()


