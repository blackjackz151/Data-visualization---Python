""" part 2 of dataviz tutorial, graphing the information we parsed"""

from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np

import parse



def visualize_days():
	"""Visualize data by day of week"""

	#grab the parsed data that we parsed earlier
	data_file = parse.parse(parse.MY_FILE, ",")

	#make a new variable "counter", from interating through each
	#line of data in the parsed data, and count how many incidents 
	#happen on each day of the week
	#iterate every dictionary value of every dictionary key set to DayOfWeek
	
	counter = Counter(item["DayOfWeek"] for item in data_file) 

	#separate the x-axis data(days of the week) from the
	#"counter variable" from the y-axis data (number of incidents for each day)

	data_list = [
					counter["Monday"],
					counter["Tuesday"], 
					counter["Wednesday"],
					counter["Thursday"],
					counter["Friday"],
					counter["Saturday"],
					counter["Sunday"]
					]
	day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

	#with that y-axis data, assign it to a matplotlib plot instance
	plt.plot(data_list)
	#create the amount of ticks neede for our x-axis, and assign the labels
	plt.xticks(range(len(day_tuple)), day_tuple)
	#save the plot
	plt.savefig("Days.png")
	#close plot file
	plt.clf()


def visualize_type():
	"""Visualize data by category in a bar graph"""

	#grab parsed data
	data_file = parse.parse(parse.MY_FILE, ",")

	#make a new counter variable from iterating through each line of parsed data and 
	#count how many incidents happen by category
	counter = Counter(item["Category"] for item in data_file)

	#set the labels which are based on the keys of our counter
	#order doesnt matter counter.keys() is fine to use
	labels = tuple(counter.keys())

	#set exactly where labels hit the x-axis
	xlocations = np.arange(len(labels)) + 0.5

	#width of each bar that will be plotted
	width = 0.5

	#assign data to a bar plot (similar to plt.plot()!)
	plt.bar(xlocations, counter.values(), width=width)

	#assign labels and tick location to x-axis
	plt.xticks(xlocations + width / 2, labels, rotation=90)

	#give some more room so the x-axis labels aren't cut off in the graph
	plt.subplots_adjust(bottom=0.4)

	#make the overall graph/figure larger
	plt.rcParams['figure.figsize'] = 14, 10

	#save the graph 
	plt.savefig("Type.png")

	#close plot figure
	plt.clf()

def main():
    visualize_days()
    visualize_type()


if __name__ == "__main__":
    main()