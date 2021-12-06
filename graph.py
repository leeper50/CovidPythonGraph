import matplotlib.pyplot as plt
import csv
from party import Party


def build_graph(files):
    plt.style.use('fivethirtyeight')
    fig, axs = plt.subplots(len(files))
    fig.set_size_inches(16, 12)
    fig.subplots_adjust(hspace=0.35)
    i = 0
    for file in files:
        with open(f'data/{file}', newline='') as myCSV:
            next(myCSV)
            data = list(csv.reader(myCSV))

            axs[i].set_title(f'Sorted by {file.strip(".csv")}')
            axs[i].set_ylim(0, 25000)

            dems = Party(data, 'D')
            axs[i].scatter(dems.xAxis, dems.yAxis, color="blue")

            reps = Party(data, 'R')
            axs[i].scatter(reps.xAxis, reps.yAxis, color="red")

            split = Party(data, 'S')
            axs[i].scatter(split.xAxis, split.yAxis, color="black")

            axs[i].plot(dems.xAxis, dems.trend_line(), "b", linewidth=1, antialiased=True)
            axs[i].plot(reps.xAxis, reps.trend_line(), "r", linewidth=1, antialiased=True)

            i = i + 1
    plt.show()
