#!/usr/bin/python

#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv
import pandas as pd


# def read_data(data):
# # COMPLETE THIS FUNCTION
# 	with open(data, 'r') as f: 
# 		reader = csv.reader(f)
# 		for row in reader: 
# 			parsed_data = row
# 			print(parsed_data)
			
# 			df= pd.DataFrame(parsed_data)
# 			print(df)

# 			#difference = float(goals) - float(goals_allowed)
# 			# print(difference)

# 	# def get_min_score_difference(self, parsed_data):
# 	# # COMPLETE THIS FUNCTION
# 		# parsed_data.pop(0)
# 			# goals = [x[5] for x in parsed_data]
# 			# goals_allowed = [x[6] for x in parsed_data]
# 			# return min([float(x) - float(y) for x, y in zip(goals, goals_allowed)])



# # 	def get_team(self, index_value, parsed_data):
# # 	# COMPLETE THIS FUNCTION

# read_data("football.csv")

data = pd.read_csv('football.csv')

data1 = data[['Team', 'Goals', 'Goals Allowed']]
for1 = data['Goals']
againist = data['Goals Allowed']

print(data1)

#finds the difference between the for goals and against goals
diff = for1 - againist

#find the index with the minimum diff 
index = diff.argmin()

#print the name of the team with the corresponding minimum difference
print(data1.ix[index]['Team'])




