import sqlite3
import pandas as pd

connection = sqlite3.connect('data-files/customers.db')

customers_data = pd.read_sql('select * from customers', connection)

new_row = {'year_joined': '2000', 'customer_name': 'Roberta Santos', 'occupation': 'Journalist'}

new_row_data = customers_data.append(new_row, ignore_index=True)

print(new_row_data)

connection.close()