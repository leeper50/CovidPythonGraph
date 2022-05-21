# future additions:
# roll the csv files into a single file, try filling arrays at once instead of looping
# get census data from file and incorporate into graph_data

import graph
import csvManipulation
import covidData


covidData.get()

combined_csv = csvManipulation.combine_csv()
# problems :
# cant graph just 1 plot, list needs item[2] to function
graph_list = [
    ['Density', 'Cases per 100k', 'President'],
    # ['Density', 'Cases per 100k', 'Governor'],
    # ['Density', 'Cases per 100k', 'Legislature'],
    ['Population', 'Total Cases', 'President'],
]

graph.build_graph(combined_csv, graph_list, True)
