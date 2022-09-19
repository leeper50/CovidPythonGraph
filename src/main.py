from graph import GraphWindow, Graph
from csvManipulation import get_csv
from pandas import DataFrame


def main() -> None:
    graph_list: list[Graph] = [
        Graph(["Density", "Cases per 100k"]),
        Graph(["Density", "Cases per 100k", "President"], trendline=True),
        # Graph(["Density", "Cases per 100k", "Governor"], trendline=True),
        # Graph(["Density", "Cases per 100k", "Legislature"], trendline=True)
    ]
    combined_csv: DataFrame = get_csv()
    GraphWindow(combined_csv, graph_list).build_window()


if __name__ == "__main__":
    main()
