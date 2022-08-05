import numpy as np
import matplotlib.pyplot as plt

class GraphWindow():
    plt.style.use("fivethirtyeight")
    party_dict: dict[str, str] = {
        "D": "blue",
        "R": "red",
        "S": "purple"
    }

    # use object to store instance variables
    def __init__(self, dataframe, list_of_graphs) -> None:
        self.dataframe = dataframe
        self.list_of_graphs = list_of_graphs
        self.fig, self.axs = plt.subplots(len(list_of_graphs))
        if len(list_of_graphs) == 1:
            self.axs = np.reshape(self.axs, 1)
        self.fig.set_size_inches(12, 8)
        self.fig.subplots_adjust(hspace=0.35)

    # construct window based on number of graphs present in the list of graphs
    def build_window(self, Trendline=True) -> None:
        graph_id = 0
        for graph_params in self.list_of_graphs:
            self.build_graph(graph_params, graph_id, Trendline)
            graph_id = graph_id + 1
        plt.show()
        
    # this method iterates through the list of graphs and builds each graph
    def build_graph(self, graph_params, graph_id, Trendline) -> None:
        def plot(xAxis, yAxis, color):
            self.axs[graph_id].scatter(data_xAxis, data_yAxis, color=color)
            if Trendline and not data_xAxis == []:
                p = np.poly1d(np.polyfit(xAxis, yAxis, 1))
                self.axs[graph_id].plot(xAxis, p(xAxis), color, linewidth=1, antialiased=True)

        if (len(graph_params) == 3):
            xaxis, yaxis, voting_record = graph_params
            self.axs[graph_id].set_title(f"{xaxis} by {yaxis} colored by {voting_record}")
            for party, party_color in GraphWindow.party_dict.items():
                df = self.dataframe[self.dataframe[voting_record] == party]
                data_xAxis = df[f"{xaxis}"].tolist()
                data_yAxis = df[f"{yaxis}"].tolist()
                plot(data_xAxis, data_yAxis, party_color)
        else:
            xaxis, yaxis = graph_params
            color = "black"
            self.axs[graph_id].set_title(f"{xaxis} by {yaxis}")
            data_xAxis = self.dataframe[xaxis].tolist()
            data_yAxis = self.dataframe[yaxis].tolist()
            plot(data_xAxis, data_yAxis, color)
