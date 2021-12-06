# future additions:
# make a web scrapper to get the data from
# https://usafacts.org/visualizations/coronavirus-covid-19-spread-map/
# or
# https://www.statista.com/statistics/1109004/coronavirus-covid19-cases-rate-us-americans-by-state/
# roll the csv files into a single file, try filling arrays at once instead of looping

import graph
import csvManipulation

csvManipulation.get_population_csv()
combined_csv = csvManipulation.combine_csv('Population')
# problems :
# cant graph just 1 plot, list needs item[2] to function
list = [
   # ['Density', 'Cases per 100k', 'President'],
   # ['Density', 'Cases per 100k', 'Governor'],
    ['Density', 'Cases per 100k', 'Legislature'],
    ['Population', 'Cases per 100k', ''],
]

graph.build_graph(combined_csv, list)
