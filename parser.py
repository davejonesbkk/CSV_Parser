
# -*- coding: utf-8 -*-

"""
Football: The football.csv file contains the results from the English Premier League. The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of goals scored for and against each team in that season (so Arsenal scored 79 goals against opponents, and had 36 goals scored against them). Write a program to read the file, then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.
Weather: In weather.csv you’ll find daily weather data. Write a program to read the file, then output the day number (column one) with the smallest temperature spread (the maximum temperature is the second column, the minimum the third column).
See if you can write the same program to solve both questions.
Test Driven Development!
"""

import csv

import pandas as pd 

import numpy as np 


class ParserScores(object):

	def league_goals(self, the_file):

		teams = []

		d = pd.read_csv(the_file)

		goals = d['Goals'].sum()

		#print out each team and its goal difference for the season
		for index, row in d.iterrows():
			goals_difference = (row['Team'], row['Goals'] - row['Goals Allowed'])
			teams.append(goals_difference)

		print(teams)

		#Separate just the goals difference total for each team
		goals_sum = ([i[1] for i in teams])

		
		#Sort the list using abs by cloest to 0
		sorted_goals = sorted(goals_sum, key = lambda x: abs(x))

		lowest = sorted_goals[0]

		print(lowest)

		for i in teams:
			if i[1] == lowest:
				print(i[0], 'Had the lowest goal difference with ', i[1], ' goals')

		return the_file

if __name__ == '__main__':
	scores = ParserScores()
	data = scores.league_goals('football.csv')



