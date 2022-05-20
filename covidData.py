from genericpath import exists
from time import ctime
from os import path
import urllib.request
import pandas as pd
import datetime as dt


def get():
    covid_data_url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    stored_data = "data/nyt_case_progress.csv"

    # pull file
    if not exists(stored_data):
        urllib.request.urlretrieve(covid_data_url, stored_data)

    # update daily
    file_last_modified = ctime(path.getmtime(stored_data))
    today_weekday = dt.datetime.today().strftime("%a")
    if not file_last_modified.__contains__(today_weekday):
        urllib.request.urlretrieve(covid_data_url, stored_data)

    # load all data into frame and sort
    not_states_list = ["American Samoa", "District of Columbia", "Northern Mariana Islands",
                       "Guam", "Puerto Rico", "Virgin Islands"]
    df = pd.read_csv(stored_data)
    not_states = df.query(f"state == {not_states_list}")
    df = df.drop(index=not_states.index, columns=["date", "fips"])

    # build most recent results
    results = df.drop_duplicates("state", keep="last")
    results.columns = ["State", "Total Cases", "Deaths"]

    # export results as csv
    results.to_csv("data/graph_data/03_total_cases.csv", index=False)
