
# -*- coding: utf-8 -*-

"""
Football: The football.csv file contains the results from the English Premier League. The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of goals scored for and against each team in that season (so Arsenal scored 79 goals against opponents, and had 36 goals scored against them). Write a program to read the file, then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.
Weather: In weather.csv you’ll find daily weather data. Write a program to read the file, then output the day number (column one) with the smallest temperature spread (the maximum temperature is the second column, the minimum the third column).
See if you can write the same program to solve both questions.
Test Driven Development!
"""

import csv

import pandas as pd 

with open('football.csv', newline='') as fp:
	football = csv.reader(fp, delimiter=' ', quotechar='|')
	for row in football:
		print(', '.join(row))

