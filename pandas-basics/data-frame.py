import pandas as pd

column = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009]
column2 = ["Bob", "Alice", "Kiegraard", "Lybiana", "Object", "Javasson", 0, 0, 0, 0]

# column2 can only be attached to a DataFrame IF it has the same length as all the other columns at the DF
titled_column = {'numbers': column,
                 'names': column2}  # the column list will be appended into the "numbers" key in the dict
data = pd.DataFrame(titled_column)
print(data)  # this organizes the column list in a table


