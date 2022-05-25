from numpy import double

import pandas as pd
import io
import requests


def getPopulationData():
    census_data_url = "https://api.census.gov/data"

    # update daily or grab for the first time
    request = govtApiCall(census_data_url)

    col_names = ["State", "Population", "Density", "Fips"]
    
    # load data to frame
    df = pd.DataFrame(columns=col_names, data=request.json()[1:])

    # drop non-states
    not_states_list = ["District of Columbia", "Puerto Rico"]
    not_states = df.query(f"State == {not_states_list}")
    df = df.drop(index=not_states.index, columns=["Fips"])

    # assign pop. density rank
    df["Density"] = df["Density"].astype(double)
    df = df.sort_values(by="Density", ascending=False)
    df["Density"] = [i for i in range(1, 51)]

    return df

# grabs covid data from a github repo by the NewYorkTimes
def getCovidData():
    covid_data_url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"

    response = requests.Session().get(covid_data_url)
    df = pd.read_csv(io.StringIO(response.text), sep=",")

    # load all data into frame and drop non-states
    not_states_list = ["American Samoa", "District of Columbia", "Northern Mariana Islands",
                    "Guam", "Puerto Rico", "Virgin Islands"]
    not_states = df.query(f"state == {not_states_list}")
    df = df.drop(index=not_states.index, columns=["date", "fips"])

    # keep only recent results
    results = df.drop_duplicates("state", keep="last")
    results.columns = ["State", "Total Cases", "Deaths"]

    return results

# get population data from census
def govtApiCall(HOST):
    year = "2021"
    dataset = "pep/population"
    base_url = "/".join([HOST, year, dataset])
    predicates = {}
    get_vars = ["NAME", "POP_2021", "DENSITY_2021"]
    predicates["get"] = ",".join(get_vars)
    predicates["for"] = "STATE:*"
    return requests.get(base_url, params=predicates)
