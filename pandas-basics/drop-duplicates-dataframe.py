import pandas as pd

data_read = pd.read_csv('entries-duplicates.csv')
print('number of entries: ', len(data_read))
data_dropped = data_read.drop_duplicates(subset=['name'])
print('number of entries: ', len(data_dropped))
print(data_dropped)
