import os
import pandas as pd


def get_population_csv():
    not_states = ["Puerto Rico", "District of Columbia", "Guam[8]", "U.S. Virgin Islands[9]",
                  "American Samoa[10]", "Northern Mariana Islands[11]"]

    df = pd.read_csv('data/table-1.csv', usecols=['State or territory', 'Census population[7][a]'])
    df.columns = ['State', 'Population']
    df = df.iloc[1:57, :]
    for item in not_states:
        index = df[df['State'] == item].index
        df.drop(index, inplace=True)
    df.reset_index(drop=True, inplace=True)
    df['Population'] = df['Population'].str.replace(',', '').astype(int)
    df.to_csv('data/temp/01_population.csv', index=False)


def combine_csv(sortby='Population'):
    list1 = os.listdir('data/temp')
    list2 = []
    for item in list1:
        list2.append(pd.read_csv(f'data/temp/{item}'))

    output = list2[0]
    for i in range(1, len(list2)):
        output = pd.merge(output, list2[i], on='State')
    output = output.sort_values(by=sortby, ascending=False)
    output.to_csv(r'data/combined.csv', index=False)
    return output
