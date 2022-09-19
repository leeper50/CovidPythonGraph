from dataclasses import dataclass, field
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class Graph:
    list: list[str]
    trendline: bool = field(kw_only=True, default=False)

class GraphWindow:
    plt.style.use("fivethirtyeight")
    party_dict = {
        "D": "blue",
        "R": "red",
        "S": "purple"
    }

    # contains window settings
    def __init__(self, dataframe, graphs: list[Graph]) -> None:
        GraphWindow.df = dataframe
        self.graphs: list[Graph] = graphs
        fig, self.axs = plt.subplots(len(graphs))
        fig.set_size_inches(12, 8)
        fig.subplots_adjust(hspace=0.25)
        if len(graphs) == 1:
            self.axs = np.reshape(self.axs, 1)

    # construct window based on number of graphs present in the list of graphs
    def build_window(self) -> None:
        for id, graph in enumerate(self.graphs):
            self.__build_plot(id, graph)
        plt.show()

    # builds plots for each graph in the window
    def __build_plot(self, id: int, graph: Graph) -> None:
        def plot(df, color):
            x = df[xaxis].tolist()
            y = df[yaxis].tolist()
            self.axs[id].scatter(x, y, color=color)
            if graph.trendline and x:
                p = np.poly1d(np.polyfit(x, y, 1))
                self.axs[id].plot(x, p(x), color, linewidth=1, antialiased=True) 

        
        if (len(graph.list) == 3):
            xaxis, yaxis, voting_record = graph.list
            self.axs[id].set_title(f"{xaxis} by {yaxis} colored by {voting_record}")
            for party, color in GraphWindow.party_dict.items():
                df = GraphWindow.df[GraphWindow.df[voting_record] == party]
                plot(df, color)
        else:
            xaxis, yaxis = graph.list
            color = "black"
            self.axs[id].set_title(f"{xaxis} by {yaxis}")
            df = GraphWindow.df
            plot(df, color)
            
