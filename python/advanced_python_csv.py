import pandas as pd 
from collections import Counter
import csv
import re

data = pd.read_csv('faculty.csv', skipinitialspace =True)


def emailscsv(dataframe):
	emails = data['email'].tolist()
	a = open('email.csv', 'w')

	#put emails into columns
	for email in emails:
		data1= "\n".join(emails)
		print(data1)
	a.write(data1)
	a.close()

emailscsv(data)