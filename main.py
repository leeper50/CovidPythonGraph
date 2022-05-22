# future additions:
# roll the csv files into a single file, try filling arrays at once instead of looping
# get census data from file and incorporate into graph_data
# consider making a Graph class where each graph is created and added to the GraphWindow class

# problems :
# single graph implementation is really bad and duplicates much code
# trendline should be created on a per graph basis

import graph
import csvManipulation
import covidData


covidData.get()

combined_csv = csvManipulation.combine_csv()
graph_list = [
    # ["Density", "Cases per 100k", "President"],
    ["Density", "Cases per 100k", "Governor"],
    ["Density", "Cases per 100k", "Legislature"],
    # ["Population", "Total Cases"],
]

test = graph.GraphWindow(combined_csv, graph_list)
test.build_graph()
test.show_graph()