import pandas as pd

data = pd.read_csv("tenants_avg.csv")

# printing a data file from another directory
data_file = pd.read_csv('data-files/data.csv')

print(data)
print("\n")
print(data_file.head(10))  # return parameter indexes, same for tails
# to remove the unnamed: 0 column state index=False into the line that creates the data frame
