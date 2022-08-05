from os import path
from datetime import datetime
import pandas as pd
import dataDownloader


COMBINED_FILE = "data/combined.csv"


# combine all the source data into one file
# add new columns based on data in file
def get_csv(sort_key="State") -> pd.DataFrame:
    if not path.exists(COMBINED_FILE) or not checkDate(COMBINED_FILE):
        pop_data: pd.DataFrame = dataDownloader.getPopulationData()
        covid_data: pd.DataFrame = dataDownloader.getCovidData()
        politics_data: pd.DataFrame = pd.read_csv("data/politics.csv")

        merged_data: pd.DataFrame = pd.merge(pop_data, covid_data, on="State")
        merged_data = pd.merge(merged_data, politics_data, on="State")
        merged_data = merged_data.sort_values(by=sort_key)
        merged_data["Population"] = merged_data["Population"].astype(int)
        merged_data["Cases per 100k"] = round(merged_data["Total Cases"] / merged_data["Population"] * 100000)
        merged_data["Deaths per 100k"] = round(merged_data["Deaths"] / merged_data["Population"] * 100000)
        merged_data.to_csv(COMBINED_FILE, index=False)
        return merged_data
    return pd.read_csv(COMBINED_FILE)


# return true if file has been updated today
def checkDate(file) -> bool:
    file_last_modified: datetime = datetime.fromtimestamp(path.getmtime(file))
    file_last_modified: str = file_last_modified.strftime("%Y-%m-%d")
    
    today: str = datetime.today().strftime("%Y-%m-%d")
    if file_last_modified == today:
        return True