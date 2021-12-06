import graph

# future additions:
# make a web scrapper to get the data from
# https://usafacts.org/visualizations/coronavirus-covid-19-spread-map/
# or
# https://www.statista.com/statistics/1109004/coronavirus-covid19-cases-rate-us-americans-by-state/

files = ["governor.csv", "legislature.csv", "president.csv"]
graph.build_graph(files)
