# single_graph and multi_graph must exist seperately as the 
# axs object can either be a list of object or an object itself
# meaning that it must be handled differently


import matplotlib.pyplot as plt
from numpy import polyfit, poly1d

class GraphWindow():
    plt.style.use("fivethirtyeight")
    party_map = {
        "D": "blue",
        "R": "red",
        "S": "purple"
    }

    # use object to store instance variables
    def __init__(self, dataframe, list_of_graphs, trendline=True):
        self.dataframe = dataframe
        self.list_of_graphs = list_of_graphs
        self.fig, self.axs = plt.subplots(len(list_of_graphs))
        self.fig.set_size_inches(12, 8)
        self.fig.subplots_adjust(hspace=0.35)

    # construct window based on number of graphs present in the list of graphs
    def build_graph(self):
        num_graphs = len(self.list_of_graphs)
        if num_graphs == 1:
            self.single_graph(self.list_of_graphs[0])
        else:
            print(self.axs)
            graph_id = 0
            for graph_params in self.list_of_graphs:
                self.multi_graph(graph_params, graph_id)
                graph_id = graph_id + 1

    # self.axs is a single graph and is built without iteration
    def single_graph(self, graph_params, trendline=True):
        def trend_line(xAxis, yAxis, color):
            p = poly1d(polyfit(xAxis, yAxis, 1))
            self.axs.plot(xAxis, p(xAxis), color, linewidth=1, antialiased=True)
        if (len(graph_params) == 3):
            xaxis, yaxis, color = graph_params
            self.axs.set_title(f"{xaxis} by {yaxis} colored by {color}")
            for party, party_color in GraphWindow.party_map.items():
                df = self.dataframe[self.dataframe[color] == party]
                data_xAxis = df[f"{xaxis}"].tolist()
                data_yAxis = df[f"{yaxis}"].tolist()
                self.axs.scatter(data_xAxis, data_yAxis, color=party_color)
                if trendline and not data_xAxis == []:
                    trend_line(data_xAxis, data_yAxis, party_color)
        else:
            xaxis, yaxis = graph_params
            self.axs.set_title(f"{xaxis} by {yaxis}")
            data_xAxis = self.dataframe[xaxis].tolist()
            data_yAxis = self.dataframe[yaxis].tolist()
            self.axs.scatter(data_xAxis, data_yAxis, color="black")
            if trendline and not data_xAxis == []:
                trend_line(data_xAxis, data_yAxis, "black")

    # self.axs is a list of graphs and is iterated over to create each graph
    def multi_graph(self, graph_params, graph_id, trendline=True):
        def trend_line(graph_id, xAxis, yAxis, color):
            p = poly1d(polyfit(xAxis, yAxis, 1))
            self.axs[graph_id].plot(xAxis, p(xAxis), color, linewidth=1, antialiased=True)
        if (len(graph_params) == 3):
            xaxis, yaxis, color = graph_params
            self.axs[graph_id].set_title(f"{xaxis} by {yaxis} colored by {color}")
            for party, party_color in GraphWindow.party_map.items():
                df = self.dataframe[self.dataframe[color] == party]
                data_xAxis = df[f"{xaxis}"].tolist()
                data_yAxis = df[f"{yaxis}"].tolist()
                self.axs[graph_id].scatter(data_xAxis, data_yAxis, color=party_color)
                if trendline and not data_xAxis == []:
                    trend_line(graph_id, data_xAxis, data_yAxis, party_color)
        else:
            xaxis, yaxis = graph_params
            self.axs[graph_id].set_title(f"{xaxis} by {yaxis}")
            data_xAxis = self.dataframe[xaxis].tolist()
            data_yAxis = self.dataframe[yaxis].tolist()
            self.axs[graph_id].scatter(data_xAxis, data_yAxis, color="black")
            if trendline and not data_xAxis == []:
                trend_line(graph_id, data_xAxis, data_yAxis, "black")

    # display the window
    def show_graph(self):
        plt.show()