import pandas as pd

# CSV files and JSON files will be read as DataFrames

data_frame = pd.read_csv('./data-files/data.csv')

# print(data_frame.to_string())

# without the to_string() method, the print(data_frame) method will return only the first 5 and last 5 rows

print(data_frame)

# using the following line we can change the max amount of lines that can be printed

print(pd.options.display.max_rows)
pd.options.display.max_rows = 256  # changing the max_row rule to 256
print(pd.options.display.max_rows)

print(data_frame)

