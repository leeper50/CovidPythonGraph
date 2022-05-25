# future additions:
# consider making a Graph class where each graph is created and added to the GraphWindow class
# allow for user input
# show user potential axes for the graph and color options
# update graph in real time when user submits change

# problems :
# trendline should be created on a per graph basis
# check time function will not run if a week has passed

import graph
import csvManipulation

def main():
    combined_csv = csvManipulation.get_csv()
    graph_list = [
        ["Density", "Cases per 100k", "President"],
        ["Density", "Cases per 100k", "Governor"],
        # ["Density", "Deaths per 100k", "President"],
        ["Population", "Total Cases"],
    ]

    test = graph.GraphWindow(combined_csv, graph_list)
    test.build_window()
    test.show_window()

if __name__ == "__main__":
    main()