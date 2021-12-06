import matplotlib.pyplot as plt
from numpy import polyfit, poly1d


class Party:
    def __init__(self, dataframe, xaxis, yaxis, party='', color=''):
        self.xAxis = []
        self.yAxis = []
        try:
            if color == "":
                self.xAxis = dataframe[xaxis].tolist()
                self.yAxis = dataframe[yaxis].tolist()
            else:
                df = dataframe[dataframe[color] == party]
                self.xAxis = df[f'{xaxis}'].tolist()
                self.yAxis = df[f'{yaxis}'].tolist()
                del df
                print()
        except SyntaxError:
            print(f"No items matching '{party}' in list")

    def trend_line(self):
        z = polyfit(self.xAxis, self.yAxis, 1)
        p = poly1d(z)
        return p(self.xAxis)


def build_graph(dataframe, list, trendline=True):
    plt.style.use('fivethirtyeight')
    fig, axs = plt.subplots(len(list))
    fig.set_size_inches(16, 12)
    fig.subplots_adjust(hspace=0.35)

    i = 0
    for item in list:
        if not item[2] == "":
            axs[i].set_title(f'{item[0]} by {item[1]} colored by {item[2]}')
            dems = Party(dataframe, item[0], item[1], 'D', item[2])
            axs[i].scatter(dems.xAxis, dems.yAxis, color="blue")
            reps = Party(dataframe, item[0], item[1], 'R', item[2])
            axs[i].scatter(reps.xAxis, reps.yAxis, color="red")
            split = Party(dataframe, item[0], item[1], 'S', item[2])
            axs[i].scatter(split.xAxis, split.yAxis, color="black")
            if trendline:
                axs[i].plot(dems.xAxis, dems.trend_line(), "b", linewidth=1, antialiased=True)
                axs[i].plot(reps.xAxis, reps.trend_line(), "r", linewidth=1, antialiased=True)
        else:
            axs[i].set_title(f'{item[0]} by {item[1]}')
            data = Party(dataframe, item[0], item[1])
            axs[i].scatter(data.xAxis, data.yAxis, color="black")
            print()
        i = i + 1

    plt.show()
