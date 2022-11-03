import sqlite3
import pandas as pd

# how to drop columns and rows from a table using dataframes

connection = sqlite3.connect('data-files/customers.db')
cursor = connection.cursor()

customers_data = pd.read_sql('select * from customers', connection)

# axis=1 means the column, while axis=0 means then rows
no_year_customers_dataframe = customers_data.drop('year_joined', axis=1)
print(no_year_customers_dataframe, "\n")

remove_row = customers_data.iloc[0:2]  # index 2 exclusive
print(remove_row)

remove_row = no_year_customers_dataframe.iloc[1:2]  # just takes the index 1
print("\n", remove_row)

connection.close()