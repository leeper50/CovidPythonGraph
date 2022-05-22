import os
import pandas as pd

def combine_csv(sort_key="State"):
    list1 = os.listdir("data/graph_data")
    list2 = []
    for item in list1:
        list2.append(pd.read_csv(f"data/graph_data/{item}"))

    output = list2[0]
    for i in range(1, len(list2)):
        output = pd.merge(output, list2[i], on="State")
    output = output.sort_values(by=sort_key, ascending=True)
    output["Cases per 100k"] = round(output["Total Cases"] / output["Population"] * 100000)
    output["Deaths per 100k"] = round(output["Deaths"] / output["Population"] * 100000)
    output.to_csv("data/combined.csv", index=False)
    return output

