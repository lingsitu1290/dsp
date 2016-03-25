#PLACE YOUR CODE HERE

import pandas as pd 
from collections import Counter
import csv
import re

data = pd.read_csv('faculty.csv', skipinitialspace =True)

#Find how many different degrees there are, and their frequencies: Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.
#Find how many different titles there are, and their frequencies: Ex: Assistant Professor, Professor
#Search for email addresses and put them in a list. Print the list of email addresses.

def numofdegrees(dataframe):
	#converted degree to a list 	
	degrees = data['degree'].tolist()
	#separate lists items with multiple items by space 	
	degrees = [y for x in degrees for y in x.split(' ')]
	
	#Cleaning the data: for each item in degrees list, remove . and space
	degree_list = []
	for degree in degrees:
		degree =degree.replace(".","")
		degree_list.append(degree)
	degreecount = Counter(degree_list)
	print(degreecount)


def numoftitles(dataframe):
	titles = data['title'].tolist()
	title_list= []
	for title in titles:
		#Cut the last three words (of Biostatistics)
		title = title.rsplit(' ',2)[0]
		title_list.append(title)
	titlecount = Counter(title_list)
	print(titlecount)


def emails(dataframe):
	emails = data['email'].tolist()

	domain_list = []
	for email in emails: 
		domains = email.split("@")[1]
		domain_list.append(domains)

	emailcount = Counter(domain_list)
	print(emailcount)

#Exporting emails to a csv file 
def emailscsv(dataframe):
	emails = data['email'].tolist()
	a = open('email.csv', 'w')

	#put emails into columns
	for email in emails:
		data1= "\n".join(emails)
		print(data1)
	a.write(data1)
	a.close()

numofdegrees(data)
numoftitles(data)
emails(data)
emailscsv(data)
