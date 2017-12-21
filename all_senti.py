
import csv
import nltk

import tkinter as tk
from tkinter import *

from tkinter import font
from tkinter import messagebox
import pickle 


def processSentence(sentenece):
	sentenece=sentenece.lower()
	return sentenece

def getFeatureVector(sentenece):
	
	featureVector=[]
	words=sentenece.split(" ")
	
	
	for w in words:
	
		featureVector.append(w.lower())
	return featureVector

def extract_features(sentenece):
    sentenece_words = set(sentenece)
    features = {}
    for word in featureList:
        features['contains(%s)' % word] = (word in sentenece_words)
    return features

def featurelistAndArray():
    featureList=[]
    inputsenteneces=csv.reader(open('data.csv','r'),delimiter=",")


    senteneces=[]
    for row in inputsenteneces:
	    sentenece=row[0]
	    sentiment=row[2]
	
	
	    processedsentenece=processSentence(sentenece)
	 
	    featureVector=getFeatureVector(processedsentenece)
	    featureList.extend(featureVector)

	    senteneces.append((featureVector,sentiment))


    featureList=list(set(featureList))
    return (featureList,senteneces)
featureList=featurelistAndArray()[0]
senteneces=featurelistAndArray()[1]


def show():
    top = Tk()
    RTitle=top.title("Sentiment analyzer")
    RWidth=top.winfo_screenwidth()/2
    RHeight=top.winfo_screenheight()/2
    top.geometry("%dx%d+0+0" % (RWidth, RHeight))


    L1 = Label(top, text="Enter the sentence you want to check",font=("Helvetica", 20))
    L1.place(x=90, y=50)
    E1 = Entry(top, bd =3)
    E1.place(x=130, y=150,width=400,height=50)
    def get():
    	testsentenece=E1.get()
    	processed=processSentence(testsentenece)
    	classifier_f=open("naive.pickle","rb")
    	NBClassifier=pickle.load(classifier_f)
    	classifier_f.close()
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




    def info():
    	messagebox.showinfo("Information",'Used Algorithm:	Naive Bayes\nTraining Data set:	1629 sentneces\nTest Data set:	100 senteneces\nAccuracy of algorithm: 82%\nSource Code and Documentation: http://bit.ly/2oVbKJU')
    

    img=tk.PhotoImage(file="info.png")
    B3=Button(top,text="info",command=info,image=img,borderwidth=0)
    B3.place(x=580, y=0,width=150,height=50)
    top.mainloop() 



def accuracychecker():
	counter=0
	inputTest=csv.reader(open('TestData.csv','r'))
	for row in inputTest:
		sentenece=row[0]
		sentiment=row[3]
		testsentenece=sentenece
		processed=processSentence(testsentenece)
		training_set=nltk.classify.util.apply_features(extract_features,senteneces)
		NBClassifier=nltk.NaiveBayesClassifier.train(training_set)
		result=NBClassifier.classify(extract_features(getFeatureVector(processed)))
		if result==sentiment:
			counter+=1
		else:
			counter=counter
	print(counter)


#main
show()




'''training_set=nltk.classify.util.apply_features(extract_features,senteneces)

NBClassifier=nltk.NaiveBayesClassifier.train(training_set)

save_classifier=open("naive.pickle","wb")
pickle.dump(NBClassifier,save_classifier)
save_classifier.close()'''



