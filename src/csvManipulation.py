from datetime import datetime
from functools import reduce
from os import path
from pandas import DataFrame, merge, read_csv
from dataDownloader import getCovidData, getPopData


COMBINED_FILE = "data/combined.csv"


# combine all the source data into one file
# add new columns based on data in file
def get_csv(sort_key="State") -> DataFrame:
    if path.exists(COMBINED_FILE) and checkDate(COMBINED_FILE):
        return read_csv(COMBINED_FILE)
    data: list[DataFrame] = [getCovidData(), getPopData(),
                             read_csv("data/politics.csv")]

    merged_data: DataFrame = (reduce(lambda left, right: merge(left, right, on="State"), data)
                              .sort_values(by=sort_key))
    merged_data["Population"] = merged_data["Population"].astype(int)
    merged_data["Cases per 100k"] = round(
        merged_data["Total Cases"] / merged_data["Population"] * 100000)
    merged_data["Deaths per 100k"] = round(
        merged_data["Deaths"] / merged_data["Population"] * 100000)
    merged_data.to_csv(COMBINED_FILE, index=False)
    return merged_data


# return true if file has been updated today
def checkDate(file) -> bool:
    last_modified: datetime = datetime.fromtimestamp(path.getmtime(file))
    last_modified: str = last_modified.strftime("%Y-%m-%d")
    today: str = datetime.today().strftime("%Y-%m-%d")
    if last_modified == today:
        return True
    return False
