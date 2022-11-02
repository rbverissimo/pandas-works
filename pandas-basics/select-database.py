import pandas as pd
import sqlite3

connection = sqlite3.connect("data-files/customers.db")
cursor = connection.cursor()

customers_data = pd.read_sql('select * from customers', connection)

print(customers_data)
print("\n")

# applying a filter to the customers_data dataframe
journalist_dataframe = customers_data[customers_data['occupation'] == 'Journalist']
print(journalist_dataframe)

# replacing Journalist for Communication
communication_dataframe = journalist_dataframe.replace('Journalist', 'Communication')
print("\n", communication_dataframe)


connection.close()