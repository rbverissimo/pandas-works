import pandas as pd

column = [1000, 1001, 1002, 1003]
titled_column = {'numbers': column}  # the column list will be appended into the "numbers" key in the dict
data = pd.DataFrame(titled_column)
print(data)  # this organizes the column list in a table


