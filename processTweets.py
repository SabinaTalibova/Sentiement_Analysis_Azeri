import re



	
	


filetoprocess=open('data1.txt','r')
line=filetoprocess.readline().split(",")


while filetoprocess:
	
	print(line[0])

