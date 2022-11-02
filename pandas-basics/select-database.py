import pandas as pd
import sqlite3

connection = sqlite3.connect("data-files/customers.db")
cursor = connection.cursor()

customers_data = pd.read_sql('select * from customers', connection)

print(customers_data)
print("\n")
journalist_dataframe = customers_data[customers_data['occupation'] == 'Journalist']
print(journalist_dataframe)


connection.close()