import pandas as pd
import datetime as dt
from time import ctime
from os import path

import dataDownloader

COMBINED_FILE = "data/combined.csv"

# combine all the source data into one file
# add new columns based on data in file
def get_csv(sort_key="State"):
    if not path.exists(COMBINED_FILE) or checkDate(COMBINED_FILE):
        pop_data = dataDownloader.getPopulationData()
        covid_data = dataDownloader.getCovidData()
        politics_data = pd.read_csv("data/politics.csv")

        merged_data = pd.merge(pop_data, covid_data, on="State")
        merged_data = pd.merge(merged_data, politics_data, on="State")
        merged_data = merged_data.sort_values(by=sort_key)
        merged_data["Population"] = merged_data["Population"].astype(int)
        merged_data["Cases per 100k"] = round(merged_data["Total Cases"] / merged_data["Population"] * 100000)
        merged_data["Deaths per 100k"] = round(merged_data["Deaths"] / merged_data["Population"] * 100000)
        merged_data.to_csv(COMBINED_FILE, index=False)
        return merged_data
    return pd.read_csv(COMBINED_FILE)


# return false if file has not been updated today
def checkDate(file):
    file_last_modified = ctime(path.getmtime(file))
    today_weekday = dt.datetime.today().strftime("%a")
    if not file_last_modified.__contains__(today_weekday):
        return False