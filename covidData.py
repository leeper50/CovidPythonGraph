from genericpath import exists
from numpy import arange
from time import ctime
from os import path
import urllib
import pandas as pd
import datetime as dt


def get():
    covid_data_url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"

    # pull file
    if not exists("us-states.csv"):
        urllib.request.urlretrieve(covid_data_url, "us-states.csv")

    # update daily
    file_last_modified = ctime(path.getmtime("us-states.csv"))
    today_weekday = dt.datetime.today().strftime('%a')
    if not file_last_modified.__contains__(today_weekday):
        urllib.request.urlretrieve(covid_data_url, "us-states.csv")

    # load all data into frame and sort
    not_states_list = ['American Samoa', 'District of Columbia', 'Northern Mariana Islands',
                       'Guam', 'Puerto Rico', 'Virgin Islands']
    df = pd.read_csv("us-states.csv")
    not_states = df.query(f"state == {not_states_list}")
    df = df.drop(index=not_states.index, columns=['date', 'fips'])

    # build most recent results
    results = df.drop_duplicates('state', keep="last")
    results.index = arange(1, len(results) + 1)

    # export results as csv
    results.to_csv('TotalCovidCasesByState.csv', index=False)
    print(results)
