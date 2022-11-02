import sqlite3
import pandas as pd

connection = sqlite3.connect('data-files/customers.db')
cursor = connection.cursor()

customers_data = pd.read_sql('select * from customers', connection)

# axis=1 means the column, while axis=0 means then rows
no_year_customers_dataframe = customers_data.drop('year_joined', axis=1)
print(no_year_customers_dataframe)

connection.close()