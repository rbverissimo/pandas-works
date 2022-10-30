import pandas as pd

data = pd.read_csv("tenants_avg.csv")
print(data)
# to remove the unnamed: 0 column state index=False into the line that creates the data frame
