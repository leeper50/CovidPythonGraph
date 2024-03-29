from pandas import DataFrame, read_csv
import io
import requests

# gets population data for all 50 states


def getPopData() -> DataFrame:
    # build api request
    url = "https://api.census.gov/data/2021/pep/population"
    predicates = {}
    predicates["get"] = "NAME,POP_2021,DENSITY_2021"
    predicates["for"] = "STATE:*"
    request = requests.get(url, params=predicates)

    # load data to frame
    col_names: list[str] = ["State", "Population", "Density", "Fips"]
    df: DataFrame = DataFrame(columns=col_names, data=request.json()[1:])

    # drop non-states
    not_states_list: list[str] = ["District of Columbia", "Puerto Rico"]
    not_states: DataFrame = df.query(f"State == {not_states_list}")
    df = df.drop(index=not_states.index, columns=["Fips"])

    # assign pop. density rank
    df["Density"] = df["Density"].astype(float)
    df = df.sort_values(by="Density", ascending=False)
    df["Density"] = [i for i in range(1, 51)]
    return df


# grabs covid data from a github repo by the NewYorkTimes
def getCovidData() -> DataFrame:
    covid_data_url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"

    response: requests.Response = requests.Session().get(covid_data_url)
    df: DataFrame = read_csv(io.StringIO(response.text), sep=",")

    # load all data into frame and drop non-states
    not_states_list: list[str] = ["American Samoa", "District of Columbia", "Northern Mariana Islands",
                                  "Guam", "Puerto Rico", "Virgin Islands"]
    not_states: DataFrame = df.query(f"state == {not_states_list}")
    df = df.drop(index=not_states.index, columns=["date", "fips"])

    # keep only recent results
    results: DataFrame = df.drop_duplicates("state", keep="last")
    results.columns = ["State", "Total Cases", "Deaths"]
    return results
