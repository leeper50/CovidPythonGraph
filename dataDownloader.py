from genericpath import exists
from time import ctime
from os import path
import urllib.request
from numpy import double
import pandas as pd
import datetime as dt

import requests

# grabs covid data from a github repo by the NewYorkTimes
def getCovidData():
    covid_data_url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    file_loc = "data/nyt_case_progress.csv"

    # update daily or grab for the first time
    if not exists(file_loc) or checkDate(file_loc):
        urllib.request.urlretrieve(covid_data_url, file_loc)

    # load all data into frame and drop non states
    not_states_list = ["American Samoa", "District of Columbia", "Northern Mariana Islands",
                       "Guam", "Puerto Rico", "Virgin Islands"]
    df = pd.read_csv(file_loc)
    not_states = df.query(f"state == {not_states_list}")
    df = df.drop(index=not_states.index, columns=["date", "fips"])

    # keep only recent results
    results = df.drop_duplicates("state", keep="last")
    results.columns = ["State", "Total Cases", "Deaths"]

    # export results as csv
    results.to_csv("data/graph_data/03_total_cases.csv", index=False)


def getPopulationData():
    file_loc = "data/graph_data/01_population_stats.csv"

    # update daily or grab for the first time
    if not exists(file_loc) or checkDate(file_loc):
        request = govtApiCall()

        col_names = ["State", "Population", "Density", "Fips"]
        not_states_list = ["District of Columbia", "Puerto Rico"]
        
        df = pd.DataFrame(columns=col_names, data=request.json()[1:])

        # drop non-states
        not_states = df.query(f"State == {not_states_list}")
        df = df.drop(index=not_states.index, columns=["Fips"])

        # assign pop. density rank
        df["Density"] = df["Density"].astype(double)
        df = df.sort_values(by="Density", ascending=False)
        df["Density"] = [i for i in range(1, 51)]

        # resort to beautify
        df = df.sort_values(by="State")

        # output to storage
        df.to_csv(file_loc, index=False)
        
# get population data from census
def govtApiCall():
    HOST = "https://api.census.gov/data"
    year = "2021"
    dataset = "pep/population"
    base_url = "/".join([HOST, year, dataset])
    predicates = {}
    get_vars = ["NAME", "POP_2021", "DENSITY_2021"]
    predicates["get"] = ",".join(get_vars)
    predicates["for"] = "STATE:*"
    return requests.get(base_url, params=predicates)

# return false if file 
def checkDate(file):
    file_last_modified = ctime(path.getmtime(file))
    today_weekday = dt.datetime.today().strftime("%a")
    if not file_last_modified.__contains__(today_weekday):
        return False