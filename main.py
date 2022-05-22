# future additions:
# roll the csv files into a single file, try filling arrays at once instead of looping
# consider making a Graph class where each graph is created and added to the GraphWindow class
# allow for user input
# show user potential axes for the graph and color options
# update graph in real time when user submits change

# problems :
# trendline should be created on a per graph basis
# covidData uses two different time packages, and should problably have either os or genericpath

import graph
import csvManipulation
import dataDownloader

dataDownloader.getPopulationData()
dataDownloader.getCovidData()


combined_csv = csvManipulation.combine_csv()
graph_list = [
    ["Density", "Cases per 100k", "President"],
    # ["Density", "Cases per 100k", "Governor"],
    ["Density", "Deaths per 100k", "President"],
    # ["Population", "Total Cases"],
]

test = graph.GraphWindow(combined_csv, graph_list)
test.build_window()
test.show_window()

