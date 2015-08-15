# Data-visualization---Python

Different visualizations of data on line graphs, bar graphs and a map.
I used the newcoder.io tutorials to help me complete this project as I am still new to python.

This project parses data from a CSV/Excel file, renders it in JSON,
saves it to a database and then is visualised in graph form. It will also plot data on a map.

The CSV file I have used is a public crime filing in San Franscisco. 

After running the parse.py file, it will return the contents of the CSV file in a JSON format so that it is easier to plot the graphs with.

After running the graph.py file it will take the data from the output of parse.py and turn it into a line graph and a bar graph.

After running the map.py file it will create a new file, if you copy the contents into https://gist.github.com/
with file_sf.geojson as the file name it will plot the areas in San Francisco where each crime is commited/where the person was arrested.
