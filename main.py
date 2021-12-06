# future additions:
# make a web scrapper to get the data from
# https://usafacts.org/visualizations/coronavirus-covid-19-spread-map/
# or
# https://www.statista.com/statistics/1109004/coronavirus-covid19-cases-rate-us-americans-by-state/
# roll the csv files into a single file, try filling arrays at once instead of looping

import graph
import csvManipulation

csvManipulation.get_population_csv()
csvManipulation.combine_csvs()
graph.build_graph('data/combined.csv')
