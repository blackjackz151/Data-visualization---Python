"""
Data Visualization Project

Parse data from a CSV or Excel file, and render it in
JSON, save to a database, and visualize in graph form.

Part I: Taking data from a CSV/Excel file, and return it into a format
that is easier for Python to play with."""

#So we can read csv/excel files import the csv module from python standard library
import csv

#all caps is global variable, it is set to sample file
MY_FILE = "/home/jack/Projects/new-coder/dataviz/data/sample_sfpd_incident_all.csv" 


#creating a function that takes the csv file and returns a JSON like object
#a delimeter is what seperates things e.g elements/columns
#parse means to analyze or separate e.g input into more easily processed components
# a JSON file/object is just a collection of dictionaries much like pythons dictionarys


def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-like object"""

    # Open CSV file, and safely close it when we're done
    opened_file = open(raw_file)

    #Read CSV file
	#csv.reader is a function of the CSV module
	#first delimeter is referring to the name of the parameter that csv.reader needs
	#second delimter refers to the arguement that the parse function takes in
    
    # Read the CSV data
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    #The csv_data object, in Python terms, is now an iterator. In very simple terms, 
	#this means we can get each element in csv_data one at a time.

    # Setup an empty list that we add every row of data that we parse through
    parsed_data = []

    # Skip over the first line of the file for the headers
    fields = csv_data.next()

    # Iterate over each row of the csv file, zip together field -> value
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    # Close the CSV file
    opened_file.close()
    #return the parsed_data variable
    return parsed_data


def main():
	#call our parse function and give it the needed parameters
	new_data = parse(MY_FILE, ",")

	print new_data


#when running a python file from the command line, python executes all code found on it
#since the following bit is true
if __name__ == "__main__":
	main()

